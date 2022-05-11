from csv import reader
from pathlib import Path

from django.core.management.base import BaseCommand

from main.models import (AdmArea, Category, CultureObject, District,
                         StatusObject, TypeObject)


class Command(BaseCommand):
    fixture_name = str(Path(__file__).parent.parent.parent.parent
                       .joinpath('msc_data.csv').resolve())

    def handle(self, *args, **options):

        print(self.fixture_name)
        self.load_csv_fixture()

    def load_csv_fixture(self):
        """Загрузка csv-фикстуры"""

        with open(self.fixture_name, 'r') as csv_file:
            data = reader(csv_file, delimiter=';')
            next(data)
            adm_areas = set()
            districts = set()
            statuses = set()
            categories = set()
            types = set()
            prepare_data = []
            for row in data:
                (id, name, name_doc, adm_area, district, location, address,
                status, category, type, position) = row
                adm_areas.add(adm_area)
                districts.add(district)
                statuses.add(status)
                categories.add(category)
                types.add(type)
                latitude = None
                longitude = None
                if position:
                    latitude, longitude = position.strip().split(',')
                prepare_data.append(
                    (name, name_doc, adm_area, district, location, address,
                     status, category, type, latitude, longitude)
                )

            adm_areas_dict = {}
            districts_dict = {}
            statuses_dict = {}
            categories_dict = {}
            types_dict = {}

            self._add_data(adm_areas, AdmArea, adm_areas_dict)
            self._add_data(districts, District, districts_dict)
            self._add_data(statuses, StatusObject, statuses_dict)
            self._add_data(categories, Category, categories_dict)
            self._add_data(types, TypeObject, types_dict)

            for row in prepare_data:
                obj = CultureObject.objects.filter(name=row[0])
                if obj.exists():
                    continue

                adm_area_id=adm_areas_dict[row[2]] or None
                district_id = districts_dict[row[3]] or None
                status_id = statuses_dict[row[6]] or None
                category_id = categories_dict[row[7]] or None
                type_id = types_dict[row[8]] or None
                culture_object = CultureObject(
                    name=row[0],
                    ensemble_name_on_doc=row[1],
                    location=row[4],
                    addresses=row[5],
                    adm_area_id=adm_area_id,
                    district_id=district_id,
                    status_id=status_id,
                    category_id=category_id,
                    type_id=type_id,
                    lat_position=row[9],
                    long_position=row[10]
                )
                culture_object.save()

    @staticmethod
    def _add_data(data, model, data_dict):
        """
        Метод-помощник, который позволяет наполнить словари ID
        """

        for item in tuple(data):
            obj_model = model.objects.filter(name=item)

            if obj_model.exists():
                data_dict[item] = obj_model.get().id
                continue

            obj = model(name=item)
            obj.save()
            data_dict[item] = obj.id

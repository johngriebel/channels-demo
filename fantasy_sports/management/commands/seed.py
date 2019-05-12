import json

from django.core.management.base import BaseCommand

from fantasy_sports.utils import parse_player_dict


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('model', type=str)
        parser.add_argument('input_file', type=str)

    def handle(self, *args, **options):
        model = options['model']
        self.stdout.write(f"Seeding data for {model}")

        if model == 'players':
            file_path = options['input_file']
            with open(file_path, 'r') as infile:
                raw_data = json.load(infile)
            for player in raw_data:
                parse_player_dict(input_data=player)

        self.stdout.write("Complete.")

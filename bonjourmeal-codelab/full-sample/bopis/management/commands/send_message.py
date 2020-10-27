# Generated by Django 3.0.8 on 2020-10-14 03:39

# Copyright 2020 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''
A CLI tool to send messages to a specific conversation ID.
'''

from django.core.management.base import BaseCommand, CommandError
from bopis.models import *
from bopis.views import *
from bopis.view_utils import *

class Command(BaseCommand):
    help = 'Setups up the inventory with Bonjour Meal Food & Drink Items'

    def add_arguments(self, parser):
        parser.add_argument('conversation_id', nargs='+', type=str)
        parser.add_argument('message', nargs='+', type=str)

    def handle(self, *args, **options):

        conversation_id = options['conversation_id'][0]
        conv = Conversation.objects.get(id=conversation_id)
        message = options['message'][0]

        route_message(message, conv)
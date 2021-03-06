# -*- coding: utf-8 -*-
# Copyright 2016 Open Permissions Platform Coalition
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License. You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed under the License is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.

import os

from mock import patch

from onboarding.models.assets import generate_idmap


with open(os.path.join(os.path.dirname(__file__), '../fixture/transform.ttl'), 'r') as myfile:
    TRIPLES = myfile.read()

SAMPLE_DATA = {
    'data': {
        'triples': TRIPLES
    }
}


@patch('onboarding.models.assets.options')
def test_generate_idmap(options):
    options.hub_id = 'hub1'
    options.default_resolver_id = 'openpermissions.org'
    repository_id = '2e9ce79cfa710e80878920c98e076aa9'

    new_id_map = generate_idmap(SAMPLE_DATA, repository_id)
    assert len(new_id_map)

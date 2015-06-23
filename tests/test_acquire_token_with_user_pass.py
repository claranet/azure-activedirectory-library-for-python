﻿#-------------------------------------------------------------------------
# Copyright (c) Microsoft. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#--------------------------------------------------------------------------
import unittest
from adal.authentication_context import AuthenticationContext
import base64
import json
import adal

sampleParameters = {
        "tenant" : "common",
        "authorityHostUrl" : "https://login.windows.net",
        "clientId" : "04b07795-8ddb-461a-bbee-02f9e1bf7b46", # xplat's which is supposed to be in every tenant
        "username" : "crwilcox@microsoft.com",
        "password" : None
}

class Test_AcquireTokenWithUsernamePassword(unittest.TestCase):

    def setUp(self):
        self.assertIsNotNone(sampleParameters['password'], "This test cannot work without you adding a password")
        return super().setUp()

    def test_acquire_token_with_user_pass_defaults(self):
        token_response = adal.acquire_token_with_username_password(sampleParameters['username'], sampleParameters['password'])
        self.validate_token_response(token_response)

    def test_acquire_token_with_user_pass_explicit(self):
        authorityUrl = sampleParameters['authorityHostUrl'] + '/' + sampleParameters['tenant']
        resource = '00000002-0000-0000-c000-000000000000' # or 'https://management.core.windows.net/'
        token_response = adal.acquire_token_with_username_password(sampleParameters['username'], sampleParameters['password'], authorityUrl, resource, sampleParameters['clientId'])
        self.validate_token_response(token_response)

    def validate_token_response(self, token_response):
        self.assertIsNotNone(token_response)

        # token response is a dict that should have
        expected = [
            'accessToken', 'expiresIn', 'expiresOn', 'familyName', 'givenName',
            'isUserIdDisplayable', 'refreshToken', 'resource', 'tenantId', 'tokenType', 'userId'
        ]
        for i in expected:
            self.assertIsNotNone(token_response.get(i), '{} is an expected item in the token response'.format(i))
if __name__ == '__main__':
    unittest.main()

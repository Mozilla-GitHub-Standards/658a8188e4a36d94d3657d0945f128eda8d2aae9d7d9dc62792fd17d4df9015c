# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from types import FunctionType

from nose.tools import eq_, ok_

from socorrolib.unittest.testbase import TestCase

from socorrolib.app.generic_app import main
from socorrolib.app.generic_app import App

from socorrolib.app.socorro_app import SocorroApp
from socorrolib.app.socorro_app import App as SApp


#==============================================================================
class TestGenericAppModule(TestCase):

    def test_exsistance(self):
        ok_(issubclass(App, SocorroApp))
        eq_(App, SApp)
        ok_(isinstance(main, FunctionType))

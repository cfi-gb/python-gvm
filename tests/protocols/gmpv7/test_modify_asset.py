# -*- coding: utf-8 -*-
# Copyright (C) 2018 Greenbone Networks GmbH
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import unittest

from gvm.errors import RequiredArgument

from . import Gmpv7TestCase


class GmpModifyAssetTestCase(Gmpv7TestCase):
    def test_modify_asset(self):
        self.gmp.modify_asset(asset_id='a1')

        self.connection.send.has_been_called_with(
            '<modify_asset asset_id="a1">'
            '<comment></comment>'
            '</modify_asset>'
        )

    def test_modify_asset_without_asset_id(self):
        with self.assertRaises(RequiredArgument):
            self.gmp.modify_asset(asset_id=None, comment='foo')

        with self.assertRaises(RequiredArgument):
            self.gmp.modify_asset(asset_id='', comment='foo')

        with self.assertRaises(RequiredArgument):
            self.gmp.modify_asset('', comment='foo')

    def test_modify_asset_with_comment(self):
        self.gmp.modify_asset('a1', 'foo')

        self.connection.send.has_been_called_with(
            '<modify_asset asset_id="a1">'
            '<comment>foo</comment>'
            '</modify_asset>'
        )

        self.gmp.modify_asset('a1', comment='foo')

        self.connection.send.has_been_called_with(
            '<modify_asset asset_id="a1">'
            '<comment>foo</comment>'
            '</modify_asset>'
        )

        self.gmp.modify_asset('a1', '')

        self.connection.send.has_been_called_with(
            '<modify_asset asset_id="a1">'
            '<comment></comment>'
            '</modify_asset>'
        )

        self.gmp.modify_asset('a1', None)

        self.connection.send.has_been_called_with(
            '<modify_asset asset_id="a1">' '<comment/>' '</modify_asset>'
        )


if __name__ == '__main__':
    unittest.main()

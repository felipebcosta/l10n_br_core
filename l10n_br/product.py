# -*- encoding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2004-2006 TINY SPRL. (http://tiny.be) All Rights Reserved.
#
# $Id: product.py 1310 2005-09-08 20:40:15Z pinky $
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

from osv import osv, fields



#-----------------------------------------
# CST
#-----------------------------------------
class product_cst(osv.osv):
	_name = 'product.cst'
	_description = 'Situacao Tributaria'
	_columns = {
		'name' : fields.char('Código', size=4, required=True),
		'description' : fields.char('Descrição', size=64, required=True),
		}
	_order = 'name'
product_cst()

#------------------------------------
# Classificacao Fiscal
#------------------------------------
class product_clfiscal(osv.osv):
	_name = 'product.clfiscal'
	_description = 'Classificacao Fiscal'
	_columns = {
		'name' : fields.char('Código', size=10, required=True),
		'description' : fields.char('Descrição', size=128, required=True),
		}
	_order = 'name'
product_clfiscal()

#------------------------------------
# Classificacao Fiscal
#------------------------------------

class product_product(osv.osv):
    _inherit = 'product.product'
    _name = 'product.product'
    _columns = {
        'cst_id' : fields.many2one('product.cst','Situação Tributária', required=True),
		'clfiscal_id' : fields.many2one('product.clfiscal','Classificação Fiscal', required=True),
    }
product_product()





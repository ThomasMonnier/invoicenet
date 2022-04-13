# Copyright (c) 2020 Sarthak Mittal
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

FIELD_TYPES = {
    "general": 0,
    "optional": 1,
    "amount": 2,
    "date": 3
}

FIELDS = dict()

# Add the following line at the end of the file

# For example, to add a field total_amount
FIELDS["power"] = FIELD_TYPES["amount"]
FIELDS["subscription_cost"] = FIELD_TYPES["amount"]
FIELDS["conso_all"] = FIELD_TYPES["amount"]
FIELDS["amount_without_tva"] = FIELD_TYPES["amount"]
FIELDS["tva"] = FIELD_TYPES["amount"]
FIELDS["total_amount"] = FIELD_TYPES["amount"]
FIELDS["to_pay"] = FIELD_TYPES["amount"]

# # For example, to add a field invoice_date
FIELDS["last_period_all"] = FIELD_TYPES["date"]

# # For example, to add a field tax_id (which might be optional)
FIELDS["nom_copro"] = FIELD_TYPES["optional"]
FIELDS["kw_unit_cost_all"] = FIELD_TYPES["optional"]
FIELDS["acheminement"] = FIELD_TYPES["optional"]
FIELDS["compte_facturation"] = FIELD_TYPES["optional"]
FIELDS["compte_commercial"] = FIELD_TYPES["optional"]

# For example, to add a field vendor_name
FIELDS["provider_name"] = FIELD_TYPES["general"]
FIELDS["prospect_adress"] = FIELD_TYPES["general"]
FIELDS["PDL"] = FIELD_TYPES["general"]
FIELDS["current_offer"] = FIELD_TYPES["general"]
FIELDS["gaz_elec"] = FIELD_TYPES["general"]
FIELDS["acheminement"] = FIELD_TYPES["general"]
FIELDS["compte_facturation"] = FIELD_TYPES["general"]
FIELDS["compte_commercial"] = FIELD_TYPES["general"]
from odoo.tests import SavepointCase


class TestStockLocationChildren(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.stock_input = cls.env.ref("stock.stock_location_company")

    def test_stock_location_amount(self):
        self.stock_quant1 = self.env["stock.quant"].create(
            {
                "product_id": self.env.ref("product.product_delivery_01").id,
                "location_id": self.stock_input.id,
                "quantity": 60,
            }
        )
        self.stock_quant1 = self.env["stock.quant"].create(
            {
                "product_id": self.env.ref("product.product_delivery_02").id,
                "location_id": self.stock_input.id,
                "quantity": 50,
            }
        )
        self.assertEqual(self.stock_input.stock_amount, 110)

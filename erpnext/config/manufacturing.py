from frappe import _

data = [
	{
		"label": _("Documents"),
		"icon": "icon-star",
		"items": [
			{
				"type": "doctype",
				"name": "Bill of Materials",
				"description": _("Bill of Materials (BOM)"),
			},
			{
				"type": "doctype",
				"name": "Production Order",
				"description": _("Orders released for production."),
			},
			{
				"type": "doctype",
				"name": "Item",
				"description": _("All Products or Services."),
			},
			{
				"type": "doctype",
				"name": "Workstation",
				"description": _("Where manufacturing operations are carried out."),
			},
			
		]
	},
	{
		"label": _("Tools"),
		"icon": "icon-wrench",
		"items": [
			{
				"type": "doctype",
				"name": "Production Planning Tool",
				"description": _("Generate Material Requests (MRP) and Production Orders."),
			},
			{
				"type": "doctype",
				"name": "BOM Replace Tool",
				"description": _("Replace Item / BOM in all BOMs"),
			},
		]
	},
	{
		"label": _("Standard Reports"),
		"icon": "icon-list",
		"items": [
			{
				"type": "report",
				"is_query_report": True,
				"name": "Open Production Orders",
				"doctype": "Production Order"
			},
			{
				"type": "report",
				"is_query_report": True,
				"name": "Production Orders in Progress",
				"doctype": "Production Order"
			},
			{
				"type": "report",
				"is_query_report": True,
				"name": "Issued Items Against Production Order",
				"doctype": "Production Order"
			},
			{
				"type": "report",
				"is_query_report": True,
				"name": "Completed Production Orders",
				"doctype": "Production Order"
			},
		]
	},
]
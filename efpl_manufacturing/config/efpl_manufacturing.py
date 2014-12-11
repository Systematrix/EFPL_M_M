from frappe import _

def get_data():
	return [
		{
			"label": _("Manufacturing"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": " Fruit Dumping Report",
					"description": _(" Fruit Dumping Report"),
				},
				{
					"type": "doctype",
					"name": "Fruit Inward Register",
					"description": _("Fruit Inward Register"),
				},
				{
					"type": "doctype",
					"name": "Log Sheet Of Decanter",
					"description": _("Log Sheet Of Decanter"),
				},
				{
					"type": "doctype",
					"name": "Machinery Cleaning Log Sheet",
					"description": _("Machinery Cleaning Log Sheet"),
				},
				{
					"type": "doctype",
					"name": "Ripe Fruit Issue Slip",
					"description": _(" Ripe Fruit Issue Slip"),
				},
			]
		},
		{
			"label": _("Maintenance"),
			"icon": "icon-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Air Compressor Log Sheet",
					"description": _("Air Compressor Log Sheet"),
				},
				{
					"type": "doctype",
					"name": "Boiler Logsheet",
					"label": _("Boiler Log Sheet"),
					"description": _("Boiler Log Sheet"),
				},
				{
					"type": "doctype",
					"name": "Chiller Log Sheet",
					"description": _("Chiller Log Sheet"),
				},
				{
					"type": "doctype",
					"name":"DG Log Sheet",
					"description": _("DG Log Sheet"),
				},
			]
		},
	]
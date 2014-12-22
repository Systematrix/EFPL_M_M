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
		{
			"label": _("Daily Calibration Checks"),
			"icon": "icon-star",
			"items": [
			    {
					"type": "doctype",
					"name": "Calibration of Weighing Balances",
					"description": _("Calibration of Weighing Balances"),
				},
				{
					"type": "doctype",
					"name": "Calibration of Refractometer",
					"description": _("Calibration of Refractometer"),
				},
				{
					"type": "doctype",
					"name": "Standardization Of NaOH",
					"label": _("Standardization Of NaOH"),
					"description": _("Standardization Of 0.1 N NaOH Solution"),
				},
				{
					"type": "doctype",
					"name": "Calibration Of pH Meter",
					"description": _("Calibration Of pH Meter"),
				},
				{
					"type": "doctype",
					"name": "Calibration Of Metal Detector",
					"description": _("Calibration Of Metal Detector"),
				},
				{
					"type": "doctype",
					"name": "COnline Testing Report",
					"description": _("COnline Testing Report"),
				},
			]
		},
	]
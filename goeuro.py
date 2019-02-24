import requests
import json


def get_tickets_json(url, path):
    """
    (str,str) -> None
    Return the json with tickets.
    """
    text = requests.get(url)
    text = text.text
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(json.loads(text), file, indent=4)


if __name__ == "__main__":
    url = "https://www.goeuro.com/GoEuroAPI/rest/api/v5/results?direction=outbound&easy=0&eoff=v2&exclude_offsite_bus_results=false&include_segment_positions=true&search_id=1203246338&sort_by=updateTime&sort_variants=onsiteDepartureTime,outboundDepartureTime,outboundPrice,price,smart,traveltime&updated_since=0&use_recommendation=true&use_stats=true"
    get_tickets_json(url, "goeuro.json")
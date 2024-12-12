class City:
    def __init__(self, name: str) -> None:
        self._name = name
        self._routes = {}

    @property
    def name(self) -> str:
        return self._name

    @property
    def routes(self) -> dict:
        return self._routes

    def add_route(self, city: str, price: float):
        self.routes[city] = price


def find_cheapest_route(start_city: City, end_city: City) -> list[str]:
    cheapest_prices, cheapest_prev_stop = {}, {}
    cheapest_prices[start_city.name] = 0

    visited_cities, discovered_cities = {}, [start_city]

    curr_city = start_city
    while discovered_cities:
        visited_cities[curr_city.name] = True
        discovered_cities.remove(curr_city)

        for adj_city in curr_city.routes:
            price_to_adj_city = curr_city.routes.get(adj_city)

            if (adj_city.name not in visited_cities) and (
                adj_city not in discovered_cities
            ):
                discovered_cities.append(adj_city)

            price_through_curr_city = (
                cheapest_prices[curr_city.name] + price_to_adj_city
            )

            if (
                adj_city.name not in cheapest_prices
            ) or price_through_curr_city < cheapest_prices[adj_city.name]:
                cheapest_prices[adj_city.name] = price_through_curr_city
                cheapest_prev_stop[adj_city.name] = curr_city.name

        cheapest_price = float("inf")
        for city in discovered_cities:
            if cheapest_prices[city.name] < cheapest_price:
                curr_city = city
                cheapest_price = cheapest_prices[city.name]

    shortest_path = []
    curr_city_name = end_city.name
    while curr_city_name:
        shortest_path.insert(0, curr_city_name)
        curr_city_name = cheapest_prev_stop.get(curr_city_name)

    return shortest_path


if __name__ == "__main__":
    atlanta = City("atlanta")
    boston = City("boston")
    chicago = City("chicago")
    denver = City("denver")
    elpaso = City("elpaso")

    atlanta.add_route(boston, 100)
    atlanta.add_route(denver, 160)
    boston.add_route(chicago, 120)
    boston.add_route(denver, 180)
    chicago.add_route(elpaso, 80)
    denver.add_route(chicago, 40)
    denver.add_route(elpaso, 140)
    elpaso.add_route(boston, 100)

    print(find_cheapest_route(atlanta, elpaso))

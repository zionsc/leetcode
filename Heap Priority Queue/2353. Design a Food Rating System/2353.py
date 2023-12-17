class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # need ratings to see if the food is actually updated
        self.ratings = defaultdict(int)
        # need cuisine[food] = cuisine as we need o(1) access to what cuisine the food is
        self.cuisine = {}
        self.by_cuisine = defaultdict(list)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.ratings[food] = -rating
            self.cuisine[food] = cuisine
            heapq.heappush(self.by_cuisine[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        self.ratings[food] = newRating
        cuisine = self.cuisine[food]
        heapq.heappush(self.by_cuisine[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
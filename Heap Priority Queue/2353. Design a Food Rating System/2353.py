class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.ratings = defaultdict(int)
        self.cuisine = {}
        self.by_cuisine = defaultdict(list)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.ratings[food] = -rating
            self.cuisine[food] = cuisine
            heapq.heappush(self.by_cuisine[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        

    def highestRated(self, cuisine: str) -> str:
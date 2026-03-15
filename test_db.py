from database import insert_candidate, get_ranked_candidates

insert_candidate("John Doe", "Python, SQL", "4 years", 8.5)

candidates = get_ranked_candidates()

print(candidates)
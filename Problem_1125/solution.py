from functools import cache
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        people = [
            sum((1 << req_skills.index(skill)) for skill in skills) 
            for skills in people
        ]
        n = len(req_skills)
        complete_skills = (1 << n)-1
        @cache
        def rec(skills_bitset):
            if skills_bitset == complete_skills:
                return []

            result = None
            for i,person in enumerate(people):
                if person | skills_bitset > skills_bitset:
                    sub_result = rec(person | skills_bitset) + [i]
                    if result is None or len(sub_result) < len(result):
                        result = sub_result
            return result
        
        return rec(0)

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = dict()
        for match in matches:
            # win
            player = match[0]
            if player not in losses:
                losses[player] = 0
            # loss
            player = match[1]
            if player not in losses:
                losses[player] = 0
            losses[player] += 1
        
        answer = [[],[]]
        for player,loss in losses.items():
            if loss == 0:
                answer[0].append(player)
            if loss == 1:
                answer[1].append(player)

        answer[0].sort()
        answer[1].sort()
        return answer

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []

        speed_position = {}

        for i in range(len(position)):
            speed_position[position[i]] = speed[i]
        
        sort_position = sorted(speed_position)
        sort_position = sort_position[::-1]
     
        for val in sort_position:
            time = (target - val) / speed_position[val]
            if not fleet:
                fleet.append(time)
                continue
            if time <= fleet[len(fleet) - 1]:
                continue
            else:
                fleet.append(time)


        return len(fleet)
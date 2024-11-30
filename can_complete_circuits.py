"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

"""
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        current_result = last_minimum_result = 0
        best_index = 0
        
        for i in range(len(gas)):
            current_result += gas[i] - cost[i]
            if last_minimum_result > current_result:
                last_minimum_result = current_result
                best_index = i
        
        if self.candidate_accepted(best_index , gas , cost):
            return best_index
        return -1
    
    def candidate_accepted(self , candidate , gas , cost):
        total_places = len(gas)
        inventory = 0
        for i , (gas_size , cost_size) in enumerate(zip(gas , cost)):
            current_place = int(i+ candidate) % total_places
            inventory += gas[current_place] - cost[current_place]
            if inventory < 0:
                return False
        return True
        
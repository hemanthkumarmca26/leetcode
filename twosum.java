import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Hash map to store numbers and their corresponding index
        Map<Integer, Integer> numToIndex = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            
            // If the complement is already in our map, we found the pair!
            if (numToIndex.containsKey(complement)) {
                return new int[] { numToIndex.get(complement), i };
            }
            
            // Otherwise, save the current number and its index to the map
            numToIndex.put(nums[i], i);
        }
        
        // Return empty array if no solution is found (though the problem guarantees one)
        return new int[] {};
    }
}



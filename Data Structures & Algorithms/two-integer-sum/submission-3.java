class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numsDict = new HashMap<>();
        for (int i = 0; i < nums.length; i++ ) {
            if (numsDict.get(target - nums[i]) != null) {
                return new int[] {numsDict.get(target - nums[i]), i};
            }
            else {
                numsDict.put(nums[i], i);
            }
        }
        return null;
    }
}

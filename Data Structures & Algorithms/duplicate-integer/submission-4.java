class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap nums_dict = new HashMap();
        for (int i: nums){
            if (nums_dict.get(i) != null) {
                return true;
            }
            nums_dict.put(i,1);
        }
        return false;
    }
}
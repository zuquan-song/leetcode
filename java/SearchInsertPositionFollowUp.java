

public class SearchInsertPositionFollowUp {
    public int searchInsert(int[] nums, int target) {
        if (target > nums[nums.length - 1]) return nums.length;
        int l = 0, r = nums.length - 1;
        while (l < r) {
            int mid = l + (r - l)/2;
            if (nums[mid] < target) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return l;
    }

    public int searchInsert2(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int mid = l + (r - l)/2;
            if (nums[mid] >= target) r = mid - 1;
            else l = mid + 1;
        }
        return l;
    }

    public static void main(String[] args) {
        SearchInsertPositionFollowUp search = new SearchInsertPositionFollowUp();
        System.out.println(search.searchInsert2(new int[] {1,3,3,3,4,7}, 3));
        System.out.println(search.searchInsert2(new int[] {1,3,3,3,4,7}, 0));
        System.out.println(search.searchInsert2(new int[] {1,3,3,3,4,7}, 7));
        System.out.println(search.searchInsert2(new int[] {1,3,3,3,4,7}, 8));
    }
}

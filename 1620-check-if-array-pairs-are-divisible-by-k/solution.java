class Solution {
    public boolean canArrange(int[] arr, int k) {
        int[] count = new int[k];
        
        for (int num : arr) {
            int remainder = ((num % k) + k) % k;
            count[remainder]++;
        }

        if (count[0] % 2 != 0) {
            return false;
        }

        for (int i = 1; i < (k + 1) / 2; i++) {
            if (count[i] != count[k - i]) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 10, 6, 7, 8, 9};
        int k = 5;
        Solution solution = new Solution();
        boolean answer = solution.canArrange(arr, k);
        System.out.println(answer);
    }
}


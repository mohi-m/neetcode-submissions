class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(s -> s[0]));

        List<int[]> merged = new ArrayList<>();
        merged.add(intervals[0]);

        for (int[] interval: intervals) {
            int first = interval[0];
            int last = interval[1];
            int prevLast = merged.get(merged.size()-1)[1];

            if (first <= prevLast) {
                merged.get(merged.size() - 1)[1] = Math.max(last, prevLast);
            }
            else {
                merged.add(interval);
            }
        }

        return merged.toArray(new int[merged.size()][]);
    }
}

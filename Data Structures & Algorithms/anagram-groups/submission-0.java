class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> res = new HashMap<>();

        for (int i = 0; i < strs.length; i++) {
            int[] count = new int[26];
            for (char s : strs[i].toCharArray()) {
                count[s - 'a']++;
            }
            String keyName = Arrays.toString(count);
            res.putIfAbsent(keyName, new ArrayList<>());
            res.get(keyName).add(strs[i]);
        }

        return new ArrayList<>(res.values());
    }
}

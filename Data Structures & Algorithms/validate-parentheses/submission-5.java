class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> pairs = new HashMap<>();
        pairs.put('(', ')');
        pairs.put('{', '}');
        pairs.put('[', ']');

        Deque<Character> stack = new ArrayDeque<>();

        for (char ch: s.toCharArray()) {
            if (pairs.containsKey(ch)) {
                stack.push(ch);
            }
            else {
                if (!stack.isEmpty()) {
                    char top = stack.pop();
                    if (pairs.get(top) != ch) {
                        return false;
                    }
                }
                else {
                    return false;
                }
            }
        }

        return stack.isEmpty() ? true : false;
    }
}

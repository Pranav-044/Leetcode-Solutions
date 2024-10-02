import java.util.Stack;

class Solution {
    public String simplifyPath(String path) {
        Stack<String> stack = new Stack<>();
        String[] parts = path.split("/");

        for (String part : parts) {
            if (part.isEmpty() || part.equals(".")) {
                continue;
            } else if (part.equals("..")) {
                if (!stack.isEmpty()) {
                    stack.pop();
                }
            } else {
                stack.push(part);
            }
        }

        StringBuilder sb = new StringBuilder();
        for (String item : stack) {
            sb.append("/");
            sb.append(item);
        }

        return sb.length() == 0 ? "/" : sb.toString();
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String input = "/.../a/../b/c/../d/./"; 
        String string = solution.simplifyPath(input);
        System.out.println(string); // Should output: "/.../b/d"
    }
}


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }

        List<Integer> rSide = new ArrayList<>();
        this.dfs(root, rSide, 0);
        return rSide; 
        
    }

    public void dfs(TreeNode root, List<Integer> rSide, int level) {
        if (root == null) {
            return ;
        }

        if(level == rSide.size()) {
            rSide.add(root.val);
        }

        this.dfs(root.right, rSide, level + 1);
        this.dfs(root.left, rSide, level + 1);   
    }
}
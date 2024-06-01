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
    public void flatten(TreeNode root) {
        if (root == null) return;

        TreeNode currentNode = root;
        while (currentNode != null) {
            if (currentNode.left != null) {
                TreeNode last = currentNode.left;
                while (last.right != null) {
                    last = last.right;
                }

                last.right = currentNode.right;
                currentNode.right = currentNode.left;
                currentNode.left = null;
            }

            currentNode = currentNode.right;
        }
        
    }
}
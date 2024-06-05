/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode sortList(ListNode head) {
    // Sudo:
    // Step 1: Find the middle node and seperate into two lists
    // Step 2: Recursively left, right
    // Step 3: Compare and merge two nodes/list.
    // step 4: return list in sorted form.

        if (head == null || head.next == null) {
            return head;
        }

        ListNode left = head;
        ListNode right = getMid(head);

        ListNode holder = right.next;
        right.next = null;
        right = holder;

        left = this.sortList(left);
        right = this.sortList(right);

        return merge(left, right);
    }

    public ListNode getMid(ListNode head) {
        ListNode slow = head;
        ListNode fast = head.next;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        return slow;
    }

    public ListNode merge(ListNode leftList, ListNode rightList) {
        ListNode dummy = new ListNode();
        ListNode tail = dummy;

        while (leftList != null && rightList != null) {
            
            if (leftList.val < rightList.val) {
                tail.next = leftList;
                leftList = leftList.next;
            } else {
                tail.next = rightList;
                rightList = rightList.next;
            }
            tail = tail.next;
        }

        if (leftList != null) {
           tail.next = leftList;
        }

        if (rightList != null) {
            tail.next = rightList;
        }

        return dummy.next;
    }

}





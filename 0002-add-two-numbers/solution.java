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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head1 = l1;
        ListNode head2 = l2;
        ListNode head3 = new ListNode(0);
        ListNode temp = head3;
        
        int data1;
        int data2;
        
        boolean k = true;
        int carry=0;
        int digitToStore;
        while(k){
            
            if(head1 == null && head2 == null && carry==0){
                k=false;
                break;
            }
        if(head1!=null){
            data1=head1.val;
            head1=head1.next;

        }
        else{
            data1=0;
        }
        if(head2!=null){
            data2=head2.val;
            head2=head2.next;

        }
        else{
            data2=0;
        }
        digitToStore = (data1 + data2 + carry) % 10;
        
                 // what goes into the current node
carry = (data1 + data2 + carry) / 10;        // what you carry to the next node

        
     temp.next=new ListNode(digitToStore);
     temp=temp.next;
    
        }
        return head3.next;
    }
}

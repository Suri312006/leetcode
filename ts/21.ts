/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

/** given two linked lists, merge the two together sorted by their values */
function mergeTwoLists(
  list1: ListNode | null,
  list2: ListNode | null
): ListNode | null {
  //* cover some base cases
  if (!list1 && !list2) {
    return null;
  }
  if (!list2) {
    return list1;
  }
  if (!list1) {
    return list2;
  }

  let alpha = list1;
  let beta = list2;
  if (alpha.val > beta.val) {
    alpha = list2;
    beta = list1;
  }
  const first_head = alpha;
  let prev_head = alpha;
  alpha = alpha.next
  do {
      if(!alpha){
        prev_head.next = beta
        return first_head 
      }
    if (alpha.val > beta.val) {
        const curr_beta = beta
        beta=beta.next

        prev_head.next = curr_beta
        curr_beta.next = alpha
        prev_head = curr_beta
    } else {
      prev_head = alpha;
      alpha = alpha.next;
    }
  } while (beta);

  return first_head;
}

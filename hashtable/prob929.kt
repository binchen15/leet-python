/*929 Unique Email Addresses */

class Solution {
    fun numUniqueEmails(emails: Array<String>): Int {

        val ans = mutableSetOf<String>()

        for (email in emails) {
            var parts = email.split("@")
            var loc = parts[0]
            ans.add(loc.replace(".", "").split("+")[0] + "@" + parts[1])
        }

        return ans.size

    }
}

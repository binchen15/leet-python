# 937 Reorder Data in Log Files

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        def isDigitLog(log):
            return log.split()[1].isdigit()
        def isLetterLog(log):
            return log.split()[1].isalpha()
        letter_logs = filter(isLetterLog, logs)
        digit_logs = filter(isDigitLog, logs)

        def order_key(log):
            words = log.split()
            return " ".join(words[1:] + [words[0]])
        sorted_letter_logs = sorted(
            letter_logs,
            key = order_key )

        return sorted_letter_logs + digit_logs

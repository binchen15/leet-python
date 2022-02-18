class Solution:
    def dayOfYear(self, date: str) -> int:
        
        from datetime import datetime
        
        obj = datetime.strptime(date, "%Y-%m-%d")
        return obj.timetuple().tm_yday

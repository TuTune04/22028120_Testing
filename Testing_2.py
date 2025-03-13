def check_fail(score, absences): # type: ignore
    """
Kiểm tra kết quả học tập dựa trên điểm số và số buổi vắng mặt.

Đầu vào:
    - score: điểm của học sinh, float [0, 10].
    - absences: số buổi học mà học sinh vắng mặt, int [0, 10].

Yêu cầu:
    - Nếu score không nằm trong khoảng [0, 10] hoặc absences không nằm trong khoảng [0, 10], 
      hàm sẽ báo lỗi với thông báo "Thông tin không hợp lệ".
    - Nếu score >= 5 và số buổi vắng mặt <= 2, học sinh được coi là "Pass".
    - Nếu không thỏa mãn điều kiện trên, học sinh được coi là "Fail".
Hàm trả về:
    - "Pass" nếu học sinh đạt yêu cầu.
    - "Fail" nếu không đạt yêu cầu.
"""
    if score < 0 or score > 10 or absences > 10 or absences < 0:
        raise ValueError("Thông tin không hợp lệ")
    if score >= 5 and absences <= 2:
        return "Pass"
    else:
        return "Fail"
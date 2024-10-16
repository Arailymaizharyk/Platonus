W1 = 0.2  # Аудитория бағасы
W2 = 0.3  # 1-ші РК бағасы
W3 = 0.3  # 2-ші РК бағасы
W4 = 0.2  # Сессия бағасы

audience_bal = float(input("Аудитория бағасын енгізіңіз: "))
RK1_bal = float(input("1-ші РК бағасын енгізіңіз: "))
RK2_bal = float(input("2-ші РК бағасын енгізіңіз: "))
session_bal = float(input("Сессия бағасын енгізіңіз: "))
final_bal = (audience_bal * W1) + (RK1_bal * W2) + (RK2_bal * W3) + (session_bal * W4)

print(f"Студенттің соңғы бағасы: {final_bal:.2f}")

# 90 балл алу үшін қажетті бағаларды есептеу
need_bal = 90
audience_needed = (need_bal - (RK1_bal * W2 + RK2_bal * W3 + session_bal * W4)) / W1
RK1_needed = (need_bal - (audience_bal * W1 + RK2_bal * W3 + session_bal * W4)) / W2
RK2_needed = (need_bal - (audience_bal * W1 + RK1_bal * W2 + session_bal * W4)) / W3
session_needed = (need_bal - (audience_bal * W1 + RK1_bal * W2 + RK2_bal * W3)) / W4

print(f"90 балл алу үшін, бағалар: Аудитория - {audience_needed:.2f}, 1-ші РК - {RK1_needed:.2f}, "
      f"2-ші РК - {RK2_needed:.2f}, Сессия - {session_needed:.2f}")
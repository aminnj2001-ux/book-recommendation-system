# سیستم پیشنهاد کتاب - فاز اول
# پیاده‌سازی شده با روش مبتنی بر محتوا (Content-Based)

# دیتابیس ساده از کتاب‌ها
books_database = [
    {"title": "The Hobbit", "genre": "fantasy", "keywords": ["dragon", "adventure", "magic"]},
    {"title": "Dune", "genre": "science fiction", "keywords": ["space", "desert", "future"]},
    {"title": "Harry Potter", "genre": "fantasy", "keywords": ["magic", "school", "wizard"]},
    {"title": "Neuromancer", "genre": "science fiction", "keywords": ["cyberpunk", "hacker", "AI"]},
    {"title": "Foundation", "genre": "science fiction", "keywords": ["space", "empire", "math"]}
]

def get_recommendations(user_genre, user_keywords, read_books):
    recommendations = []
    
    # تبدیل کلمات کلیدی کاربر به حروف کوچک برای مقایسه بهتر
    user_keywords = [kw.lower() for kw in user_keywords]
    
    for book in books_database:
        # اگر کتاب قبلا خوانده شده، از لیست خارج شود
        if book["title"].lower() in [rb.lower() for rb in read_books]:
            continue
            
        score = 0
        
        # امتیازدهی بر اساس ژانر
        if book["genre"].lower() == user_genre.lower():
            score += 10
            
        # امتیازدهی بر اساس کلمات کلیدی
        for kw in book["keywords"]:
            if kw.lower() in user_keywords:
                score += 5
                
        # اگر امتیازی کسب کرد، به لیست اضافه شود
        if score > 0:
            recommendations.append((book["title"], score))
            
    # مرتب‌سازی لیست بر اساس امتیاز (از بیشترین به کمترین)
    recommendations.sort(key=lambda x: x[1], reverse=True)
    
    return recommendations

def main():
    print("=== به سیستم پیشنهاد کتاب خوش آمدید ===")
    
    # دریافت اطلاعات از کاربر
    genre_input = input("ژانر مورد علاقه خود را وارد کنید (مثلاً fantasy یا science fiction): ")
    keywords_input = input("کلمات کلیدی مورد علاقه را با کاما جدا کنید (مثلاً magic, space): ")
    read_books_input = input("کتاب‌هایی که قبلاً خوانده‌اید را با کاما جدا کنید (یا خالی بگذارید): ")
    
    # پردازش ورودی‌ها
    keywords_list = [k.strip() for k in keywords_input.split(",") if k.strip()]
    read_books_list = [b.strip() for b in read_books_input.split(",") if b.strip()]
    
    # دریافت پیشنهادات
    results = get_recommendations(genre_input, keywords_list, read_books_list)
    
    print("\n--- لیست کتاب‌های پیشنهادی برای شما ---")
    if results:
        for title, score in results:
            print(f"- {title} (امتیاز تطابق: {score})")
    else:
        print("متأسفانه کتابی با این مشخصات پیدا نشد.")

if __name__ == "__main__":
    main()

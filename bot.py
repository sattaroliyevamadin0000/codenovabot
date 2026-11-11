import asyncio
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

TOKEN = "9268454154:AAH6epZCXXnmAp6fATYMlaj8fPij50v4RGY"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ----------------- HELPER BUTTONS -----------------
def back_button(target="back_to_main"):
    builder = InlineKeyboardBuilder()
    builder.button(text="⬅️ Orqaga", callback_data=target)
    return builder.as_markup()

# ----------------- ASOSIY MENYU -----------------
def get_main_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="📚 O'rganish bo'limi", callback_data="menu_study")
    builder.button(text="🤖 AI imkoniyatlari", callback_data="menu_ai")
    builder.button(text="💻 Amaliyot bo'limi", callback_data="menu_practice")
    builder.button(text="📝 Bilim va rivojlanish", callback_data="menu_knowledge")
    builder.button(text="🚀 Loyihalar bo'limi", callback_data="menu_projects")
    builder.button(text="🏆 Natijalar bo'limi", callback_data="menu_results")
    builder.button(text="👤 Shaxsiy kabinet", callback_data="menu_profile")
    builder.adjust(1, 2, 2, 2)
    return builder.as_markup()

# ----------------- 1. O'RGANISH BO'LIMI -----------------
def get_study_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="📚 Dasturlash tillari (To'liq)", callback_data="study_languages")
    builder.button(text="🎓 Mening darslarim (Kengaytirilgan)", callback_data="study_my_lessons")
    builder.button(text="🎞️ Video darslar markazi (Barcha tillar)", callback_data="study_videos")
    builder.button(text="📖 IT Ensiklopediya Lug'ati", callback_data="study_dictionary")
    builder.button(text="🗺️ Roadmap (Yo'l xaritasi)", callback_data="study_roadmap")
    builder.button(text="💼 Kasb tanlash qo'llanmasi", callback_data="study_career")
    builder.button(text="⬅️ Orqaga", callback_data="back_to_main")
    builder.adjust(1, 2, 2, 1, 1)
    return builder.as_markup()

def get_languages_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="🐍 Python", callback_data="lang_python")
    builder.button(text="🌐 JavaScript", callback_data="lang_js")
    builder.button(text="🐘 PHP", callback_data="lang_php")
    builder.button(text="☕ Java", callback_data="lang_java")
    builder.button(text="⚙️ C++", callback_data="lang_cpp")
    builder.button(text="🔷 C#", callback_data="lang_csharp")
    builder.button(text="🎨 HTML & CSS", callback_data="lang_html")
    builder.button(text="🗄️ SQL", callback_data="lang_sql")
    builder.button(text="📱 Flutter / Mobile", callback_data="lang_flutter")
    builder.button(text="🚀 Go (Golang)", callback_data="lang_go")
    builder.button(text="⬅️ Orqaga", callback_data="menu_study")
    builder.adjust(2, 2, 2, 2, 2, 1)
    return builder.as_markup()

# BARCHA TILLAR UCHUN YOUTUBE VIDEO DARSLAR MENYusi
def get_video_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="▶️ Python Masterclass", url="https://www.youtube.com/results?search_query=python+noldan+uzbekcha")
    builder.button(text="▶️ JavaScript Professional", url="https://www.youtube.com/results?search_query=javascript+uzbekcha")
    builder.button(text="▶️ PHP va Laravel", url="https://www.youtube.com/results?search_query=php+laravel+uzbekcha")
    builder.button(text="▶️ Java Android Darslari", url="https://www.youtube.com/results?search_query=java+android+uzbekcha")
    builder.button(text="▶️ C++ Dasturlash", url="https://www.youtube.com/results?search_query=c%2B%2B+uzbekcha+darslar")
    builder.button(text="▶️ C# va Unity GameDev", url="https://www.youtube.com/results?search_query=c%23+unity+uzbekcha")
    builder.button(text="▶️ HTML, CSS va Web", url="https://www.youtube.com/results?search_query=html+css+javascript+uzbekcha")
    builder.button(text="▶️ SQL Ma'lumotlar bazasi", url="https://www.youtube.com/results?search_query=sql+darslari+uzbekcha")
    builder.button(text="▶️ Flutter Mobil Ilovalar", url="https://www.youtube.com/results?search_query=flutter+uzbekcha")
    builder.button(text="▶️ Go (Golang) Backend", url="https://www.youtube.com/results?search_query=golang+uzbekcha+darslar")
    builder.button(text="▶️ React.js Kutubxonasi", url="https://www.youtube.com/results?search_query=react+js+uzbekcha")
    builder.button(text="▶️ Kiberxavfsizlik (CyberSecurity)", url="https://www.youtube.com/results?search_query=kiberxavfsizlik+uzbekcha")
    builder.button(text="⬅️ Orqaga", callback_data="menu_study")
    builder.adjust(2, 2, 2, 2, 2, 2, 1)
    return builder.as_markup()

def get_interactive_lessons_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="📖 1-Modul: Algoritmlar va Mantiq", callback_data="lesson_1")
    builder.button(text="📖 2-Modul: O'zgaruvchilar va Tiplar", callback_data="lesson_2")
    builder.button(text="📖 3-Modul: Shart Operatorlari (If/Else)", callback_data="lesson_3")
    builder.button(text="📖 4-Modul: Takrorlanish (Loops)", callback_data="lesson_4")
    builder.button(text="📖 5-Modul: Funksiyalar va Scope", callback_data="lesson_5")
    builder.button(text="📖 6-Modul: OOP va Klasslar", callback_data="lesson_6")
    builder.button(text="📖 7-Modul: Xatoliklar bilan ishlash", callback_data="lesson_7")
    builder.button(text="⬅️ Orqaga", callback_data="menu_study")
    builder.adjust(1, 1, 1, 1, 1, 1, 1, 1)
    return builder.as_markup()

def get_dictionary_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="📌 A - F Atamalar (Batafsil)", callback_data="dict_af")
    builder.button(text="📌 G - M Atamalar (Batafsil)", callback_data="dict_gm")
    builder.button(text="📌 N - S Atamalar (Batafsil)", callback_data="dict_ns")
    builder.button(text="📌 T - Z Atamalar (Batafsil)", callback_data="dict_tz")
    builder.button(text="⬅️ Orqaga", callback_data="menu_study")
    builder.adjust(2, 2, 1)
    return builder.as_markup()

# ----------------- 2. AI IMKONIYATLARI -----------------
def get_ai_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="🤖 AI Ustoz", callback_data="ai_teacher")
    builder.button(text="🐞 BugHunter", callback_data="ai_bughunter")
    builder.button(text="🔍 Code Review", callback_data="ai_review")
    builder.button(text="🎤 AI Interview", callback_data="ai_interview")
    builder.button(text="⬅️ Orqaga", callback_data="back_to_main")
    builder.adjust(1, 2, 1, 1)
    return builder.as_markup()

# ----------------- 3. AMALIYOT BO'LIMI -----------------
def get_practice_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="💻 Kod Laboratoriyasi (Online Compilers)", callback_data="prac_lab")
    builder.button(text="🔀 CodeCompare (Taqqoslash)", callback_data="prac_compare")
    builder.button(text="⚡ Code Speed Test", callback_data="prac_speed")
    builder.button(text="🔥 Daily Challenge", callback_data="prac_daily")
    builder.button(text="⬅️ Orqaga", callback_data="back_to_main")
    builder.adjust(1, 2, 1, 1)
    return builder.as_markup()

def get_compiler_links():
    builder = InlineKeyboardBuilder()
    builder.button(text="🐍 Python Compiler", url="https://www.programiz.com/python-programming/online-compiler/")
    builder.button(text="🌐 JS / Web Compiler", url="https://jsfiddle.net/")
    builder.button(text="⚙️ C++ Compiler", url="https://www.onlinegdb.com/online_c++_compiler")
    builder.button(text="☕ Java Compiler", url="https://www.programiz.com/java-programming/online-compiler/")
    builder.button(text="🚀 Replit (Barcha tillar)", url="https://replit.com/")
    builder.button(text="⬅️ Orqaga", callback_data="menu_practice")
    builder.adjust(2, 2, 1, 1)
    return builder.as_markup()

# ----------------- 4. BILIM VA RIVOJLANISH -----------------
def get_knowledge_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="📝 Interaktiv Testlar (Batafsil)", callback_data="know_tests")
    builder.button(text="📊 Progress Analytics", callback_data="know_analytics")
    builder.button(text="🎯 Bilim darajasi tahlili", callback_data="know_level")
    builder.button(text="🧠 Xatolar ustida ishlash", callback_data="know_mistakes")
    builder.button(text="⬅️ Orqaga", callback_data="back_to_main")
    builder.adjust(2, 2, 1)
    return builder.as_markup()

def get_test_topics_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="🐍 Python Testi", callback_data="test_quiz_python")
    builder.button(text="🌐 JavaScript Testi", callback_data="test_quiz_js")
    builder.button(text="🗄️ SQL Testi", callback_data="test_quiz_sql")
    builder.button(text="⬅️ Orqaga", callback_data="menu_knowledge")
    builder.adjust(2, 1, 1)
    return builder.as_markup()

# ----------------- 5. LOYIHALAR BO'LIMI -----------------
def get_projects_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="🚀 Loyihalar ro'yxati", callback_data="proj_list")
    builder.button(text="➕ O'z loyihangizni qo'shing", callback_data="proj_add")
    builder.button(text="👥 Jamoaviy loyihalar (Team Hub)", callback_data="proj_team")
    builder.button(text="🐙 GitHub Portfolio", callback_data="proj_github")
    builder.button(text="⬅️ Orqaga", callback_data="back_to_main")
    builder.adjust(2, 2, 1)
    return builder.as_markup()

# ----------------- 6. NATIJALAR BO'LIMI -----------------
def get_results_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="🏆 Top Reyting", callback_data="res_rating")
    builder.button(text="📜 Sertifikat olish", callback_data="res_cert")
    builder.button(text="🌟 Yutuqlar va Nishonlar", callback_data="res_badges")
    builder.button(text="📈 Mening natijalarim", callback_data="res_my")
    builder.button(text="⬅️ Orqaga", callback_data="back_to_main")
    builder.adjust(2, 2, 1)
    return builder.as_markup()

# ----------------- 7. SHAXSIY KABINET -----------------
def get_profile_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="👤 Mening profilim", callback_data="prof_info")
    builder.button(text="🌐 Tilni o'zgartirish (UZ/RU/EN)", callback_data="prof_lang")
    builder.button(text="⚙️ Tizim Sozlamalari", callback_data="prof_settings")
    builder.button(text="⬅️ Orqaga", callback_data="back_to_main")
    builder.adjust(2, 1, 1)
    return builder.as_markup()

def get_language_select_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="🇺🇿 O'zbekcha", callback_data="set_lang_uz")
    builder.button(text="🇷🇺 Русский", callback_data="set_lang_ru")
    builder.button(text="🇬🇧 English", callback_data="set_lang_en")
    builder.button(text="⬅️ Orqaga", callback_data="menu_profile")
    builder.adjust(3, 1)
    return builder.as_markup()


# ----------------- HANDLERS -----------------

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    user_name = message.from_user.full_name
    username = f"@{message.from_user.username}" if message.from_user.username else "Mavjud emas"
    
    welcome_text = (
        f"Assalomu alaykum, **{user_name}**!\n"
        "🚀 **CodeNova AI** — Professional ta'lim va kodlash platformasiga xush kelibsiz!\n"
        "Quyidagi boshqaruv panelidan kerakli bo'limni tanlang:"
    )
    await message.answer(welcome_text, reply_markup=get_main_menu(), parse_mode="Markdown")

@dp.callback_query(F.data == "back_to_main")
async def back_to_main(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "🏠 **Asosiy menyu**\nKerakli yo'nalishni tanlang:",
        reply_markup=get_main_menu(),
        parse_mode="Markdown"
    )

# --- ASOSIY BO'LIMLARGA O'TISH ---
@dp.callback_query(F.data == "menu_study")
async def open_study(callback: types.CallbackQuery):
    await callback.message.edit_text("📚 **O'rganish bo'limi**\nBarcha nazariy va amaliy modullar ro'yxati:", reply_markup=get_study_menu(), parse_mode="Markdown")

@dp.callback_query(F.data == "menu_ai")
async def open_ai(callback: types.CallbackQuery):
    await callback.message.edit_text("🤖 **AI imkoniyatlari**\nSun'iy intellekt yordamchilaridan birini tanlang:", reply_markup=get_ai_menu(), parse_mode="Markdown")

@dp.callback_query(F.data == "menu_practice")
async def open_practice(callback: types.CallbackQuery):
    await callback.message.edit_text("💻 **Amaliyot bo'limi**\nReal kod yozish va onlayn muhitlar:", reply_markup=get_practice_menu(), parse_mode="Markdown")

@dp.callback_query(F.data == "menu_knowledge")
async def open_knowledge(callback: types.CallbackQuery):
    await callback.message.edit_text("📝 **Bilim va rivojlanish bo'limi**:", reply_markup=get_knowledge_menu(), parse_mode="Markdown")

@dp.callback_query(F.data == "menu_projects")
async def open_projects(callback: types.CallbackQuery):
    await callback.message.edit_text("🚀 **Loyihalar bo'limi**:", reply_markup=get_projects_menu(), parse_mode="Markdown")

@dp.callback_query(F.data == "menu_results")
async def open_results(callback: types.CallbackQuery):
    await callback.message.edit_text("🏆 **Natijalar bo'limi**:", reply_markup=get_results_menu(), parse_mode="Markdown")

@dp.callback_query(F.data == "menu_profile")
async def open_profile(callback: types.CallbackQuery):
    await callback.message.edit_text("👤 **Shaxsiy kabinet**:", reply_markup=get_profile_menu(), parse_mode="Markdown")


# --- O'RGANISH BO'LIMI: DASTURLASH TILLARI ---
@dp.callback_query(F.data == "study_languages")
async def study_languages(callback: types.CallbackQuery):
    await callback.message.edit_text("📚 **Dasturlash tillari markazi**\n\nTilingizni tanlang:", reply_markup=get_languages_menu(), parse_mode="Markdown")

@dp.callback_query(F.data.startswith("lang_"))
async def language_details(callback: types.CallbackQuery):
    lang = callback.data.split("_")[1]
    details = {
        "python": (
            "🐍 **Python Dasturlash Tili**\n\n"
            "• **To'liq tushuncha:** Python — yuqori darajadagi, o'qish oson va sintaksisi sodda bo'lgan umumiy maqsadli dasturlash tili.\n"
            "• **Qo'llanish sohalari:** Sun'iy intellekt (AI), Machine Learning, Data Science, Veb dasturlash (Django, FastAPI), Avtomatlashtirish.\n"
            "• **Kod namunasi:**\n```python\ndef salom(ism):\n    return f'Salom, {ism}!'\nprint(salom('Madina'))\n```"
        ),
        "js": (
            "🌐 **JavaScript & TypeScript**\n\n"
            "• **To'liq tushuncha:** Veb sahifalarga interaktivlik bag'ishlovchi asosiy dasturlash tili.\n"
            "• **Qo'llanish sohalari:** Frontend (React.js, Vue.js), Backend (Node.js, Express), Mobile ilovalar.\n"
            "• **Kod namunasi:**\n```javascript\nconst salom = (ism) => `Salom, ${ism}!`;\nconsole.log(salom('Madina'));\n```"
        ),
        "php": (
            "🐘 **PHP & Laravel Framework**\n\n"
            "• **To'liq tushuncha:** Veb server tomonida ishlaydigan va dinamik saytlarni ta'minlovchi til.\n"
            "• **Qo'llanish sohalari:** Dinamik saytlar, internet do'konlar, CMS (WordPress) va API lar.\n"
            "• **Kod namunasi:**\n```php\n<?php\n$ism = 'Madina';\necho 'Salom, ' . $ism;\n?>\n```"
        ),
        "java": (
            "☕ **Java & Enterprise**\n\n"
            "• **To'liq tushuncha:** Kuchli tiplashtirilgan, xavfsiz va obyektga yo'naltirilgan dasturlash tili.\n"
            "• **Qo'llanish sohalari:** Android mobil ilovalar, yirik bank tizimlari, korporativ dasturlar.\n"
            "• **Kod namunasi:**\n```java\npublic class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Salom Java\");\n    }\n}\n```"
        ),
        "cpp": (
            "⚙️ **C++ Yuqori unumdorlik**\n\n"
            "• **To'liq tushuncha:** Tez ishlaydigan, tizimli dasturlash va o'yinlar yaratishda tengsiz til.\n"
            "• **Qo'llanish sohalari:** O'yin dvigatellari (Unreal Engine), operatsion tizimlar, murakkab algoritmlar.\n"
            "• **Kod namunasi:**\n```cpp\n#include <iostream>\nusing namespace std;\nint main() {\n    cout << \"C++ Active\" << endl;\n    return 0;\n}\n```"
        ),
        "csharp": (
            "🔷 **C# (C-Sharp) .NET**\n\n"
            "• **To'liq tushuncha:** Microsoft tomonidan yaratilgan, Unity o'yin dvigateli va Windows dasturlari uchun asosiy til.\n"
            "• **Kod namunasi:**\n```csharp\nusing System;\nclass Program {\n    static void Main() {\n        Console.WriteLine(\"Hello C#\");\n    }\n}\n```"
        ),
        "html": (
            "🎨 **HTML5 & CSS3**\n\n"
            "• **To'liq tushuncha:** Veb sahifaning karkasi (HTML) va uning tashqi ko'rinishi, dizayni (CSS)."
        ),
        "sql": (
            "🗄️ **SQL (Ma'lumotlar bazasi)**\n\n"
            "• **To'liq tushuncha:** Relyatsion ma'lumotlar omborlari (PostgreSQL, MySQL) bilan ishlash uchun so'rovlar tili.\n"
            "• **Kod namunasi:**\n```sql\nSELECT * FROM users WHERE status = 'active';\n```"
        ),
        "flutter": (
            "📱 **Flutter & Dart**\n\n"
            "• **To'liq tushuncha:** Google tomonidan yaratilgan, bitta kod bazasi yordamida ham Android, ham iOS uchun ilovalar yaratish texnologiyasi."
        ),
        "go": (
            "🚀 **Go (Golang)**\n\n"
            "• **To'liq tushuncha:** Google tomonidan ishlab chiqilgan, yuqori tezlikdagi va mikroservislar uchun mo'ljallangan zamonaviy backend tili."
        )
    }
    await callback.message.edit_text(details.get(lang, "Ma'lumot topilmadi."), reply_markup=back_button("study_languages"), parse_mode="Markdown")


# --- MENING DARSLARIM: TO'LIQ PROFESSIONAL QO'LLANMA ---
@dp.callback_query(F.data == "study_my_lessons")
async def study_my_lessons(callback: types.CallbackQuery):
    text = (
        "🎓 **Mening darslarim — To'liq Professional Kurs**\n\n"
        "Dasturlashni noldan boshlab professional darajagacha o'rganishingiz uchun kengaytirilgan nazariya va amaliy misollar:\n"
        "O'rganishni boshlash uchun modulni tanlang:"
    )
    await callback.message.edit_text(text, reply_markup=get_interactive_lessons_menu(), parse_mode="Markdown")

@dp.callback_query(F.data.startswith("lesson_"))
async def interactive_lesson_content(callback: types.CallbackQuery):
    l_id = callback.data.split("_")[1]
    lessons = {
        "1": (
            "📖 **1-Modul: Algoritmlar va Mantiqiy Fikrlash**\n\n"
            "• **To'liq Nazariya:** Algoritm — bu muammoni hal qilishga qaratilgan aniq qadamlar ketma-ketligidir.\n"
            "• **Turlari:** Chiziqli, tarmoqlanuvchi va takrorlanuvchi algoritmlar.\n"
            "• **Amaliy Masala:** Berilgan sonning tub yoki tub emasligini aniqlash."
        ),
        "2": (
            "📖 **2-Modul: O'zgaruvchilar va Ma'lumot turlari**\n\n"
            "• **To'liq Nazariya:** O'zgaruvchilar xotirada ma'lumot saqlash idishlari hisoblanadi.\n"
            "• **Asosiy turlar:** `int`, `float`, `str`, `bool`, `list`, `dict`."
        ),
        "3": (
            "📖 **3-Modul: Shart Operatorlari (If, Elif, Else)**\n\n"
            "• **To'liq Nazariya:** Dastur jarayonida turli shartlarga qarab qaror qabul qilish uchun qo'llaniladi.\n"
            "• **Namuna:**\n```python\nif score >= 80:\n    print('A''lo')\nelse:\n    print('Harakat qiling')\n```"
        ),
        "4": (
            "📖 **4-Modul: Takrorlanish Operatorlari (Loops)**\n\n"
            "• **To'liq Nazariya:** `for` va `while` sikllari orqali bir xil kod qismini avtomatik takrorlaymiz."
        ),
        "5": (
            "📖 **5-Modul: Funksiyalar va Scope**\n\n"
            "• **To'liq Nazariya:** Kodni modullarga bo'lish, `def` orqali funksiya yaratish va `return` qilish."
        ),
        "6": (
            "📖 **6-Modul: OOP (Obyektga Yo'naltirilgan Dasturlash)**\n\n"
            "• **To'liq Nazariya:** Inkapsulatsiya, vorislik, polimorfizm va abstraksiya tamoyillari."
        ),
        "7": (
            "📖 **7-Modul: Xatoliklar bilan ishlash (Try / Except)**\n\n"
            "• **To'liq Nazariya:** Dastur to'xtab qolmasligi uchun istisno holatlarni ushlash."
        )
    }
    await callback.message.edit_text(lessons.get(l_id, "Dars topilmadi."), reply_markup=back_button("study_my_lessons"), parse_mode="Markdown")

@dp.callback_query(F.data == "study_videos")
async def study_videos(callback: types.CallbackQuery):
    text = "🎞️ **Video Darslar Markazi**\n\nBarcha dasturlash tillari va yo'nalishlari bo'yicha YouTube darsliklarini ochish uchun tanlang:"
    await callback.message.edit_text(text, reply_markup=get_video_menu(), parse_mode="Markdown")

@dp.callback_query(F.data == "study_dictionary")
async def study_dictionary(callback: types.CallbackQuery):
    text = "📖 **IT Ensiklopediya va Atamalar Lug'ati**\n\nKategoriyani tanlang:"
    await callback.message.edit_text(text, reply_markup=get_dictionary_menu(), parse_mode="Markdown")

@dp.callback_query(F.data.startswith("dict_"))
async def dictionary_content(callback: types.CallbackQuery):
    part = callback.data.split("_")[1]
    dicts = {
        "af": "📖 **A - F Atamalar (Batafsil)**\n\n• **API:** Dasturlarning o'zaro muloqot interfeysi.\n• **Backend:** Server va ma'lumotlar bazasi.\n• **Bug:** Koddagi xatolik.\n• **Docker:** Konteynerlash vositasi.",
        "gm": "📖 **G - M Atamalar (Batafsil)**\n\n• **Git:** Versiya boshqaruvi.\n• **HTTP:** Veb protokoli.\n• **IDE:** Dasturlash muhiti.",
        "ns": "📖 **N - S Atamalar (Batafsil)**\n\n• **Node.js:** JS server muhiti.\n• **OOP:** Obyektga yo'naltirilgan dasturlash.\n• **REST API:** Standartlashtirilgan veb xizmat.\n• **SQL:** Ma'lumotlar bazasi tili.",
        "tz": "📖 **T - Z Atamalar (Batafsil)**\n\n• **UI/UX:** Interfeys va dizayn.\n• **Variable:** O'zgaruvchi."
    }
    await callback.message.edit_text(dicts.get(part, "Topilmadi."), reply_markup=back_button("study_dictionary"), parse_mode="Markdown")

@dp.callback_query(F.data == "study_roadmap")
async def study_roadmap(callback: types.CallbackQuery):
    text = "🗺️ **Roadmap — To'g'ri Yo'l Xaritasi**\n\n• **Backend:** Python -> SQL -> FastAPI -> Docker\n• **Frontend:** HTML/CSS -> JS -> React.js"
    await callback.message.edit_text(text, reply_markup=back_button("menu_study"), parse_mode="Markdown")

@dp.callback_query(F.data == "study_career")
async def study_career(callback: types.CallbackQuery):
    text = "💼 **Kasb tanlash qo'llanmasi**\n\n• Backend Dev\n• Frontend Dev\n• Data Science & AI"
    await callback.message.edit_text(text, reply_markup=back_button("menu_study"), parse_mode="Markdown")


# --- 2. AI BO'LIMI ---
@dp.callback_query(F.data == "ai_teacher")
async def ai_teacher(callback: types.CallbackQuery):
    await callback.message.edit_text("🤖 **AI Ustoz**\n\nSavolingizni yuboring, sun'iy intellekt tushuntirib beradi.", reply_markup=back_button("menu_ai"), parse_mode="Markdown")

@dp.callback_query(F.data == "ai_bughunter")
async def ai_bughunter(callback: types.CallbackQuery):
    await callback.message.edit_text("🐞 **BugHunter**\n\nXatoli kodni yuboring.", reply_markup=back_button("menu_ai"), parse_mode="Markdown")

@dp.callback_query(F.data == "ai_review")
async def ai_review(callback: types.CallbackQuery):
    await callback.message.edit_text("🔍 **Code Review**\n\nKodingiz sifatini tekshirish uchun yuboring.", reply_markup=back_button("menu_ai"), parse_mode="Markdown")

@dp.callback_query(F.data == "ai_interview")
async def ai_interview(callback: types.CallbackQuery):
    await callback.message.edit_text("🎤 **AI Interview**\n\nTexnik suhbat simulyatsiyasiga tayyorlaning.", reply_markup=back_button("menu_ai"), parse_mode="Markdown")


# --- 3. AMALIYOT BO'LIMI ---
@dp.callback_query(F.data == "prac_lab")
async def prac_lab(callback: types.CallbackQuery):
    await callback.message.edit_text("💻 **Kod Laboratoriyasi**\n\nOnlayn IDE va kompilyatorlar:", reply_markup=get_compiler_links(), parse_mode="Markdown")

@dp.callback_query(F.data == "prac_compare")
async def prac_compare(callback: types.CallbackQuery):
    await callback.message.edit_text("🔀 **CodeCompare**\n\nTillarni solishtirish.", reply_markup=back_button("menu_practice"), parse_mode="Markdown")

@dp.callback_query(F.data == "prac_speed")
async def prac_speed(callback: types.CallbackQuery):
    await callback.message.edit_text("⚡ **Code Speed Test**\n\nTezkor kod yozish musobaqasi.", reply_markup=back_button("menu_practice"), parse_mode="Markdown")

@dp.callback_query(F.data == "prac_daily")
async def prac_daily(callback: types.CallbackQuery):
    await callback.message.edit_text("🔥 **Daily Challenge**\n\nKunlik algoritmik masala.", reply_markup=back_button("menu_practice"), parse_mode="Markdown")


# --- 4. BILIM VA RIVOJLANISH ---
@dp.callback_query(F.data == "know_tests")
async def know_tests(callback: types.CallbackQuery):
    await callback.message.edit_text("📝 **Interaktiv Testlar**\n\nTilni tanlang:", reply_markup=get_test_topics_menu(), parse_mode="Markdown")

@dp.callback_query(F.data == "test_quiz_python")
async def quiz_python(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.button(text="A) def", callback_data="ans_correct")
    builder.button(text="B) function", callback_data="ans_wrong")
    builder.button(text="C) create", callback_data="ans_wrong")
    builder.button(text="⬅️ Orqaga", callback_data="know_tests")
    builder.adjust(3, 1)
    await callback.message.edit_text("❓ **Python Test - 1-savol**\n\nFunksiya e'lon qilish kalit so'zi?", reply_markup=builder.as_markup(), parse_mode="Markdown")

@dp.callback_query(F.data == "ans_correct")
async def ans_correct(callback: types.CallbackQuery):
    await callback.answer("✅ To'g'ri! +10 XP", show_alert=True)

@dp.callback_query(F.data == "ans_wrong")
async def ans_wrong(callback: types.CallbackQuery):
    await callback.answer("❌ Noto'g'ri javob!", show_alert=True)

@dp.callback_query(F.data == "know_analytics")
async def know_analytics(callback: types.CallbackQuery):
    await callback.message.edit_text("📊 **Progress Analytics**\n\nO'zlashtirish: 88%", reply_markup=back_button("menu_knowledge"), parse_mode="Markdown")

@dp.callback_query(F.data == "know_level")
async def know_level(callback: types.CallbackQuery):
    await callback.message.edit_text("🎯 **Bilim darajasi**\n\nSizning darajangiz: Middle Developer", reply_markup=back_button("menu_knowledge"), parse_mode="Markdown")

@dp.callback_query(F.data == "know_mistakes")
async def know_mistakes(callback: types.CallbackQuery):
    await callback.message.edit_text("🧠 **Xatolar ustida ishlash**\n\nTahlil qilindi.", reply_markup=back_button("menu_knowledge"), parse_mode="Markdown")


# --- 5. LOYIHALAR BO'LIMI ---
@dp.callback_query(F.data == "proj_list")
async def proj_list(callback: types.CallbackQuery):
    await callback.message.edit_text("🚀 **Loyihalar ro'yxati**\n\n1. Telegram Bot\n2. E-Commerce Web App", reply_markup=back_button("menu_projects"), parse_mode="Markdown")

@dp.callback_query(F.data == "proj_add")
async def proj_add(callback: types.CallbackQuery):
    await callback.message.edit_text("➕ **Loyiha qo'shish**\n\nHavolani yuboring.", reply_markup=back_button("menu_projects"), parse_mode="Markdown")

@dp.callback_query(F.data == "proj_team")
async def proj_team(callback: types.CallbackQuery):
    await callback.message.edit_text("👥 **Jamoaviy loyihalar**\n\nStartap jamoasi.", reply_markup=back_button("menu_projects"), parse_mode="Markdown")

@dp.callback_query(F.data == "proj_github")
async def proj_github(callback: types.CallbackQuery):
    await callback.message.edit_text("🐙 **GitHub Portfolio**\n\nProfil ulangan.", reply_markup=back_button("menu_projects"), parse_mode="Markdown")


# --- 6. NATIJALAR BO'LIMI ---
@dp.callback_query(F.data == "res_rating")
async def res_rating(callback: types.CallbackQuery):
    await callback.message.edit_text("🏆 **Top Reyting**\n\n1. Jasur - 2100 XP\n2. Madina - 1950 XP", reply_markup=back_button("menu_results"), parse_mode="Markdown")

@dp.callback_query(F.data == "res_cert")
async def res_cert(callback: types.CallbackQuery):
    await callback.message.edit_text("📜 **Sertifikat**\n\nKursni yakunlab raqamli sertifikat oling.", reply_markup=back_button("menu_results"), parse_mode="Markdown")

@dp.callback_query(F.data == "res_badges")
async def res_badges(callback: types.CallbackQuery):
    await callback.message.edit_text("🌟 **Yutuqlar**\n\nNishonlar ro'yxati.", reply_markup=back_button("menu_results"), parse_mode="Markdown")

@dp.callback_query(F.data == "res_my")
async def res_my(callback: types.CallbackQuery):
    await callback.message.edit_text("📈 **Mening natijalarim**\n\nUmumiy statistika.", reply_markup=back_button("menu_results"), parse_mode="Markdown")


# --- 7. SHAXSIY KABINET ---
@dp.callback_query(F.data == "prof_info")
async def prof_info(callback: types.CallbackQuery):
    user = callback.from_user
    username_str = f"@{user.username}" if user.username else "Mavjud emas"
    text = f"👤 **Shaxsiy Profil**\n\nIsm: {user.full_name}\nUsername: {username_str}\nID: `{user.id}`\nXP: 1950 XP"
    await callback.message.edit_text(text, reply_markup=back_button("menu_profile"), parse_mode="Markdown")

@dp.callback_query(F.data == "prof_lang")
async def prof_lang(callback: types.CallbackQuery):
    await callback.message.edit_text("🌐 **Tilni tanlang:**", reply_markup=get_language_select_menu(), parse_mode="Markdown")

@dp.callback_query(F.data == "prof_settings")
async def prof_settings(callback: types.CallbackQuery):
    await callback.message.edit_text("⚙️ **Sozlamalar**\n\nBildirishnomalar yoqilgan.", reply_markup=back_button("menu_profile"), parse_mode="Markdown")

@dp.callback_query(F.data.startswith("set_lang_"))
async def set_language(callback: types.CallbackQuery):
    lang_code = callback.data.split("_")[2]
    messages = {
        "uz": "🇺🇿 Til O'zbekchaga o'zgartirildi!",
        "ru": "🇷🇺 Язык изменен на Русский!",
        "en": "🇬🇧 Language changed to English!"
    }
    await callback.answer(messages.get(lang_code, "Til o'zgardi"), show_alert=True)

# ----------------- BOTNI ISHGA TUSHIRISH -----------------
async def main():
    print("CodeNova AI platformasi to'liq hajmda ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
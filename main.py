import tkinter as tk
from tkinter import messagebox
import requests

class CityListApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.translations = {
            "en": {
                "title": "Turkish Cities",
                "about": "About",
                "about_dialog": "Author: sctech-tr\nLicense: MIT",
                "change_language": "Change language",
                "search": "Search:",
                "cities_and_codes": "Turkish Cities and Car Codes",
                "cities_and_codes_tr": "Türk Şehirleri ve Plaka Kodları",
                "api_error": "Failed to retrieve city data. Please try again later."
            },
            "tr": {
                "title": "Türk Şehirleri",
                "about": "Hakkında",
                "about_dialog": "Yazar: sctech-tr\nLisans: MIT",
                "change_language": "Dili Değiştir",
                "search": "Arama:",
                "cities_and_codes": "Türk Şehirleri ve Plaka Kodları",
                "cities_and_codes_tr": "Turkish Cities and Car Codes",
                "api_error": "Bilgi sunucudan alınamadı. Lütfen daha sonra tekrar deneyiniz."
            }
        }
        self.lang = "en"
        self.title(self.translations[self.lang]["title"])
        self.geometry("400x600")
        self.cities = []
        self.api_error = False
        self.header_label = None

        self.create_widgets()
        self.fetch_and_display_city_data()

    def fetch_and_display_city_data(self):
        try:
            response = requests.get('https://turkiye-il-plakalari.gamerselimiko.workers.dev/cities')
            response.raise_for_status()
            city_lines = response.text.strip().split('\n')
            self.cities = [self.parse_city_line(line) for line in city_lines if line.strip()]
            self.api_error = False
        except requests.exceptions.RequestException as e:
            self.api_error = True
            print("Error fetching city data:", e)
            messagebox.showerror(self.translations[self.lang]["title"], self.translations[self.lang]["api_error"])
        
        self.update_city_list()

    def parse_city_line(self, line):
        parts = line.strip().split('(')
        city = parts[0].strip()
        code = parts[1].strip(')').strip()
        return {'city': city, 'code': code}

    def update_city_list(self, *args):
        search_term = self.search_var.get().lower()
        filtered_cities = [city for city in self.cities if search_term in city['city'].lower()]
        self.sorted_cities = sorted(filtered_cities, key=lambda x: x['code'])

        for widget in self.city_frame.winfo_children():
            widget.destroy()

        self.create_header()

        for city_data in self.sorted_cities:
            city_text = f"{city_data['city']} ({city_data['code']})"
            tk.Label(self.city_frame, text=city_text, font=("Arial", 10)).pack(anchor="w", padx=10, pady=2)

    def create_header(self):
        header_text = self.translations[self.lang]["cities_and_codes"]
        self.header_label = tk.Label(self.city_frame, text=header_text, font=("Arial", 12, "bold"))
        self.header_label.pack(pady=10)

    def create_widgets(self):
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)

        self.menubar.add_command(label=self.translations[self.lang]["about"], command=self.show_about)
        lang_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label=self.translations[self.lang]["change_language"], menu=lang_menu)
        lang_menu.add_command(label="English", command=lambda: self.change_language("en"))
        lang_menu.add_command(label="Türkçe", command=lambda: self.change_language("tr"))

        frame = tk.Frame(self)
        frame.pack(fill=tk.BOTH, expand=True)

        search_frame = tk.Frame(frame)
        search_frame.pack(fill=tk.X, padx=10, pady=5)

        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.update_city_list)
        search_box = tk.Entry(search_frame, textvariable=self.search_var, font=("Arial", 12))
        self.search_label = tk.Label(search_frame, text=self.translations[self.lang]["search"], font=("Arial", 12, "bold"))
        self.search_label.pack(side=tk.LEFT, padx=5)
        search_box.pack(side=tk.LEFT, fill=tk.X, expand=True)

        canvas = tk.Canvas(frame)
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        self.city_frame = tk.Frame(canvas)

        self.city_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.city_frame, anchor="nw")

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)

    def show_about(self):
        messagebox.showinfo(self.translations[self.lang]["about"], self.translations[self.lang]["about_dialog"])

    def change_language(self, lang):
        self.lang = lang
        self.title(self.translations[self.lang]["title"])
        self.update_widgets_text()
        self.update_city_list()

    def update_widgets_text(self):
        self.title(self.translations[self.lang]["title"])
        self.menubar.entryconfig(1, label=self.translations[self.lang]["about"])
        self.menubar.entryconfig(2, label=self.translations[self.lang]["change_language"])
        self.search_label.config(text=self.translations[self.lang]["search"])

if __name__ == "__main__":
    app = CityListApp()
    app.mainloop()

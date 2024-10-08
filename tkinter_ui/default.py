import tkinter as tk
from utils.config import config
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import filedialog
import os
from utils.channel import get_channel_items


class DefaultUI:

    def init_ui(self, root):
        """
        Init default UI
        """
        frame_default_open_update = tk.Frame(root)
        frame_default_open_update.pack(fill=tk.X)
        frame_default_open_update_column1 = tk.Frame(frame_default_open_update)
        frame_default_open_update_column1.pack(side=tk.LEFT, fill=tk.Y)
        frame_default_open_update_column2 = tk.Frame(frame_default_open_update)
        frame_default_open_update_column2.pack(side=tk.RIGHT, fill=tk.Y)

        self.open_update_label = tk.Label(
            frame_default_open_update_column1, text="开启更新:", width=8
        )
        self.open_update_label.pack(side=tk.LEFT, padx=4, pady=8)
        self.open_update_var = tk.BooleanVar(
            value=config.getboolean("Settings", "open_update")
        )
        self.open_update_checkbutton = ttk.Checkbutton(
            frame_default_open_update_column1,
            variable=self.open_update_var,
            onvalue=True,
            offvalue=False,
            command=self.update_open_update,
            text="(关闭则只运行结果页面服务)",
        )
        self.open_update_checkbutton.pack(side=tk.LEFT, padx=4, pady=8)

        self.open_use_old_result_label = tk.Label(
            frame_default_open_update_column2, text="使用历史结果:", width=12
        )
        self.open_use_old_result_label.pack(side=tk.LEFT, padx=4, pady=8)
        self.open_use_old_result_var = tk.BooleanVar(
            value=config.getboolean("Settings", "open_use_old_result")
        )
        self.open_use_old_result_checkbutton = ttk.Checkbutton(
            frame_default_open_update_column2,
            variable=self.open_use_old_result_var,
            onvalue=True,
            offvalue=False,
            command=self.update_open_use_old_result,
            text="(保留上次更新可用结果)",
        )
        self.open_use_old_result_checkbutton.pack(side=tk.LEFT, padx=4, pady=8)

        frame_default_source_file = tk.Frame(root)
        frame_default_source_file.pack(fill=tk.X)

        self.source_file_label = tk.Label(
            frame_default_source_file, text="模板文件:", width=8
        )
        self.source_file_entry = tk.Entry(frame_default_source_file)
        self.source_file_label.pack(side=tk.LEFT, padx=4, pady=8)
        self.source_file_entry.pack(fill=tk.X, padx=4, expand=True)
        self.source_file_entry.insert(0, config.get("Settings", "source_file"))

        frame_default_source_file_select = tk.Frame(root)
        frame_default_source_file_select.pack(fill=tk.X)

        self.source_file_button = tk.ttk.Button(
            frame_default_source_file_select,
            text="选择文件",
            command=self.select_source_file,
        )
        self.source_file_button.pack(side=tk.LEFT, padx=4, pady=0)

        frame_default_source_channels = tk.Frame(root)
        frame_default_source_channels.pack(fill=tk.X)

        self.source_channels_label = tk.Label(
            frame_default_source_channels, text="频道名称:", width=8
        )
        self.source_channels_label.pack(side=tk.LEFT, padx=4, pady=8)
        self.source_channels_text = scrolledtext.ScrolledText(
            frame_default_source_channels, height=5
        )
        self.source_channels_text.pack(
            side=tk.LEFT, padx=4, pady=8, expand=True, fill=tk.BOTH
        )
        self.source_channels_text.insert(
            tk.END, config.get("Settings", "source_channels")
        )
        self.source_channels_text.bind("<KeyRelease>", self.update_source_channels)

        frame_default_final_file = tk.Frame(root)
        frame_default_final_file.pack(fill=tk.X)

        self.final_file_label = tk.Label(
            frame_default_final_file, text="结果文件:", width=8
        )
        self.final_file_entry = tk.Entry(frame_default_final_file)
        self.final_file_label.pack(side=tk.LEFT, padx=4, pady=8)
        self.final_file_entry.pack(fill=tk.X, padx=4, expand=True)
        self.final_file_entry.insert(0, config.get("Settings", "final_file"))

        frame_default_final_file_select = tk.Frame(root)
        frame_default_final_file_select.pack(fill=tk.X)

        self.final_file_button = tk.ttk.Button(
            frame_default_final_file_select,
            text="选择文件",
            command=self.select_final_file,
        )
        self.final_file_button.pack(side=tk.LEFT, padx=4, pady=0)

        frame_default_mode = tk.Frame(root)
        frame_default_mode.pack(fill=tk.X)
        frame_default_mode_params_column1 = tk.Frame(frame_default_mode)
        frame_default_mode_params_column1.pack(side=tk.LEFT, fill=tk.Y)
        frame_default_mode_params_column2 = tk.Frame(frame_default_mode)
        frame_default_mode_params_column2.pack(side=tk.RIGHT, fill=tk.Y)

        self.open_driver_label = tk.Label(
            frame_default_mode_params_column1, text="浏览器模式:", width=12
        )
        self.open_driver_label.pack(side=tk.LEFT, padx=4, pady=8)
        self.open_driver_var = tk.BooleanVar(
            value=config.getboolean("Settings", "open_driver")
        )
        self.open_driver_checkbutton = ttk.Checkbutton(
            frame_default_mode_params_column1,
            variable=self.open_driver_var,
            onvalue=True,
            offvalue=False,
            command=self.update_open_driver,
            text="(若获取更新异常请开启)",
        )
        self.open_driver_checkbutton.pack(side=tk.LEFT, padx=4, pady=8)

        self.open_proxy_label = tk.Label(
            frame_default_mode_params_column2, text="开启代理:", width=12
        )
        self.open_proxy_label.pack(side=tk.LEFT, padx=4, pady=8)
        self.open_proxy_var = tk.BooleanVar(
            value=config.getboolean("Settings", "open_proxy")
        )
        self.open_proxy_checkbutton = ttk.Checkbutton(
            frame_default_mode_params_column2,
            variable=self.open_proxy_var,
            onvalue=True,
            offvalue=False,
            command=self.update_open_proxy,
            text="(通过代理进行更新)",
        )
        self.open_proxy_checkbutton.pack(side=tk.LEFT, padx=4, pady=8)

        frame_default_channel = tk.Frame(root)
        frame_default_channel.pack(fill=tk.X)
        frame_default_channel_column1 = tk.Frame(frame_default_channel)
        frame_default_channel_column1.pack(side=tk.LEFT, fill=tk.Y)
        frame_default_channel_column2 = tk.Frame(frame_default_channel)
        frame_default_channel_column2.pack(side=tk.RIGHT, fill=tk.Y)

        self.urls_limit_label = tk.Label(
            frame_default_channel_column1, text="频道接口数量:", width=12
        )
        self.urls_limit_label.pack(side=tk.LEFT, padx=4, pady=8)
        self.urls_limit_entry = tk.Entry(frame_default_channel_column1)
        self.urls_limit_entry.pack(side=tk.LEFT, padx=4, pady=8)
        self.urls_limit_entry.insert(15, config.getint("Settings", "urls_limit"))
        self.urls_limit_entry.bind("<KeyRelease>", self.update_urls_limit)

        self.ipv_type_label = tk.Label(
            frame_default_channel_column2, text="接口协议类型:", width=12
        )
        self.ipv_type_label.pack(side=tk.LEFT, padx=4, pady=8)
        self.ipv_type_combo = ttk.Combobox(frame_default_channel_column2)
        self.ipv_type_combo.pack(side=tk.LEFT, padx=4, pady=8)
        self.ipv_type_combo["values"] = ("ipv4", "ipv6", "all")
        self.ipv_type_combo.current(0)
        self.ipv_type_combo.bind("<<ComboboxSelected>>", self.update_ipv_type)

        frame_default_sort = tk.Frame(root)
        frame_default_sort.pack(fill=tk.X)
        frame_default_sort_column1 = tk.Frame(frame_default_sort)
        frame_default_sort_column1.pack(side=tk.LEFT, fill=tk.Y)
        frame_default_sort_column2 = tk.Frame(frame_default_sort)
        frame_default_sort_column2.pack(side=tk.RIGHT, fill=tk.Y)

        self.open_keep_all_label = tk.Label(
            frame_default_sort_column1, text="保留模式:", width=12
        )
        self.open_keep_all_label.pack(side=tk.LEFT, padx=4, pady=8)
        self.open_keep_all_var = tk.BooleanVar(
            value=config.getboolean("Settings", "open_keep_all")
        )
        self.open_keep_all_checkbutton = ttk.Checkbutton(
            frame_default_sort_column1,
            variable=self.open_keep_all_var,
            onvalue=True,
            offvalue=False,
            command=self.update_open_keep_all,
            text="(保留所有检索结果，建议手动维护时开启)",
        )
        self.open_keep_all_checkbutton.pack(side=tk.LEFT, padx=4, pady=8)

        self.open_sort_label = tk.Label(
            frame_default_sort_column2, text="开启测速排序:", width=12
        )
        self.open_sort_label.pack(side=tk.LEFT, padx=4, pady=8)
        self.open_sort_var = tk.BooleanVar(
            value=config.getboolean("Settings", "open_sort")
        )
        self.open_sort_checkbutton = ttk.Checkbutton(
            frame_default_sort_column2,
            variable=self.open_sort_var,
            onvalue=True,
            offvalue=False,
            command=self.update_open_sort,
        )
        self.open_sort_checkbutton.pack(side=tk.LEFT, padx=4, pady=8)

        frame_default_sort_params = tk.Frame(root)
        frame_default_sort_params.pack(fill=tk.X)
        frame_default_sort_params_column1 = tk.Frame(frame_default_sort_params)
        frame_default_sort_params_column1.pack(side=tk.LEFT, fill=tk.Y)
        frame_default_sort_params_column2 = tk.Frame(frame_default_sort_params)
        frame_default_sort_params_column2.pack(side=tk.RIGHT, fill=tk.Y)

        self.response_time_weight_label = tk.Label(
            frame_default_sort_params_column1, text="响应时间权重:", width=12
        )
        self.response_time_weight_label.pack(side=tk.LEFT, padx=4, pady=8)
        self.response_time_weight_entry = tk.Entry(frame_default_sort_params_column1)
        self.response_time_weight_entry.pack(side=tk.LEFT, padx=4, pady=8)
        self.response_time_weight_entry.insert(
            0, config.getfloat("Settings", "response_time_weight")
        )
        self.response_time_weight_entry.bind(
            "<KeyRelease>", self.update_response_time_weight
        )

        self.resolution_weight_label = tk.Label(
            frame_default_sort_params_column2, text="分辨率权重:", width=12
        )
        self.resolution_weight_label.pack(side=tk.LEFT, padx=4, pady=8)
        self.resolution_weight_entry = tk.Entry(frame_default_sort_params_column2)
        self.resolution_weight_entry.pack(side=tk.LEFT, padx=4, pady=8)
        self.resolution_weight_entry.insert(
            0, config.getfloat("Settings", "resolution_weight")
        )
        self.resolution_weight_entry.bind("<KeyRelease>", self.update_resolution_weight)

        frame_default_domain_blacklist = tk.Frame(root)
        frame_default_domain_blacklist.pack(fill=tk.X)

        self.domain_blacklist_label = tk.Label(
            frame_default_domain_blacklist, text="域名黑名单:", width=12
        )
        self.domain_blacklist_label.pack(side=tk.LEFT, padx=4, pady=8)
        self.domain_blacklist_text = scrolledtext.ScrolledText(
            frame_default_domain_blacklist, height=2
        )
        self.domain_blacklist_text.pack(
            side=tk.LEFT, padx=4, pady=8, expand=True, fill=tk.BOTH
        )
        self.domain_blacklist_text.insert(
            tk.END, config.get("Settings", "domain_blacklist")
        )
        self.domain_blacklist_text.bind("<KeyRelease>", self.update_domain_blacklist)

        frame_default_url_keywords_blacklist = tk.Frame(root)
        frame_default_url_keywords_blacklist.pack(fill=tk.X)

        self.url_keywords_blacklist_label = tk.Label(
            frame_default_url_keywords_blacklist, text="关键字黑名单:", width=12
        )
        self.url_keywords_blacklist_label.pack(side=tk.LEFT, padx=4, pady=8)
        self.url_keywords_blacklist_text = scrolledtext.ScrolledText(
            frame_default_url_keywords_blacklist, height=2
        )
        self.url_keywords_blacklist_text.pack(
            side=tk.LEFT, padx=4, pady=8, expand=True, fill=tk.BOTH
        )
        self.url_keywords_blacklist_text.insert(
            tk.END, config.get("Settings", "url_keywords_blacklist")
        )
        self.url_keywords_blacklist_text.bind(
            "<KeyRelease>", self.update_url_keywords_blacklist
        )

    def update_open_update(self):
        config.set("Settings", "open_update", str(self.open_update_var.get()))

    def update_open_use_old_result(self):
        config.set(
            "Settings", "open_use_old_result", str(self.open_use_old_result_var.get())
        )

    def select_source_file(self):
        filepath = filedialog.askopenfilename(
            initialdir=os.getcwd(), title="选择模板文件", filetypes=[("txt", "*.txt")]
        )
        if filepath:
            self.source_file_entry.delete(0, tk.END)
            self.source_file_entry.insert(0, filepath)
            config.set("Settings", "source_file", filepath)
            get_channel_items(change_source_path=True)
            self.source_channels_text.delete(1.0, tk.END)
            self.source_channels_text.insert(
                tk.END, config.get("Settings", "source_channels")
            )

    def update_source_channels(self, event):
        config.set(
            "Settings",
            "source_channels",
            self.source_channels_text.get(1.0, tk.END),
        )

    def select_final_file(self):
        filepath = filedialog.askopenfilename(
            initialdir=os.getcwd(), title="选择结果文件", filetypes=[("txt", "*.txt")]
        )
        if filepath:
            self.final_file_entry.delete(0, tk.END)
            self.final_file_entry.insert(0, filepath)
            config.set("Settings", "final_file", filepath)

    def update_open_driver(self):
        config.set("Settings", "open_driver", str(self.open_driver_var.get()))

    def update_open_proxy(self):
        config.set("Settings", "open_proxy", str(self.open_proxy_var.get()))

    def update_open_keep_all(self):
        config.set("Settings", "open_keep_all", str(self.open_keep_all_var.get()))

    def update_open_sort(self):
        config.set("Settings", "open_sort", str(self.open_sort_var.get()))

    def update_urls_limit(self, event):
        config.set("Settings", "urls_limit", self.urls_limit_entry.get())

    def update_response_time_weight(self, event):
        config.set(
            "Settings", "response_time_weight", self.response_time_weight_entry.get()
        )

    def update_resolution_weight(self, event):
        config.set("Settings", "resolution_weight", self.resolution_weight_entry.get())

    def update_ipv_type(self, event):
        config.set("Settings", "ipv_type", self.ipv_type_combo.get())

    def update_url_keywords_blacklist(self, event):
        config.set(
            "Settings",
            "url_keywords_blacklist",
            self.url_keywords_blacklist_text.get(1.0, tk.END),
        )

    def update_domain_blacklist(self, event):
        config.set(
            "Settings",
            "domain_blacklist",
            self.domain_blacklist_text.get(1.0, tk.END),
        )

    def update_url_keywords_blacklist(self, event):
        config.set(
            "Settings",
            "url_keywords_blacklist",
            self.url_keywords_blacklist_text.get(1.0, tk.END),
        )

    def change_entry_state(self, state):
        for entry in [
            "open_update_checkbutton",
            "open_use_old_result_checkbutton",
            "open_driver_checkbutton",
            "open_proxy_checkbutton",
            "source_file_entry",
            "source_file_button",
            "source_channels_text",
            "final_file_entry",
            "final_file_button",
            "open_keep_all_checkbutton",
            "open_sort_checkbutton",
            "urls_limit_entry",
            "response_time_weight_entry",
            "resolution_weight_entry",
            "ipv_type_combo",
            "domain_blacklist_text",
            "url_keywords_blacklist_text",
        ]:
            getattr(self, entry).config(state=state)

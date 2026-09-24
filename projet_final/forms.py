class StyledFormMixin:
    """Apply the shared visual treatment to business-form widgets."""

    field_classes = (
        "block w-full appearance-none rounded-xl border-2 border-slate-200 bg-white px-4 py-3 "
        "text-slate-900 shadow-sm transition duration-200 placeholder:text-slate-400 "
        "hover:border-border focus:border-primary focus:outline-none focus:ring-4 focus:ring-primary/20"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            existing_classes = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = (
                f"{existing_classes} {self.field_classes}".strip()
            )

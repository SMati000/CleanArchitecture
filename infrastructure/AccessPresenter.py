from useCases.SimpleMessageDTO import SimpleMessageDTO, SessionMessageDTO


class PresenterI:
    _viewModel: str

    def present(self, message: SimpleMessageDTO):
        pass

    def getViewModel(self) -> str:
        return self._viewModel


class AccessPresenter(PresenterI):
    """Override"""
    def present(self, message: SessionMessageDTO):
        self._viewModel = """<b>{title}</b>
<strong><i>{desc}</i></strong>
User: <span class="tg-spoiler">{usr}</span>
Password: <span class="tg-spoiler">{psw}</span>""" \
        .format(
            title=message.title,
            desc=message.message,
            usr=message.user,
            psw=message.password,
        )
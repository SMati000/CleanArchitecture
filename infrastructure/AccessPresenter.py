from useCases.SimpleMessageDTO import SimpleMessageDTO, SessionMessageDTO


class PresenterI:
    """
    Interface of a presenter

    Attributes:
    --------------
    viewModel: str
        message in HTML ready to be replied to the user
    
    Method
    ----------
    present(message: SimpleMessageDTO):
        generates the viewModel
    """

    _viewModel: str

    def present(self, message: SimpleMessageDTO):
        """
        generates the viewModel
        
        Parameters
        ----------
        message: SimpleMessageDTO
            The info to be displayed in the view model
        """
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
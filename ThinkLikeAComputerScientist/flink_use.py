from statefun import *
functions = StatefulFunctions()
@functions.bind(
    typename='com.example.fns/greeter',
    specs=[ValueSpec(name='seen_count', type=IntType)])
async def greet(ctx: Context, message: Message):
    name = message.as_string()
    storage = ctx.storage
    seen = storage.seen_count or 0
    storage.seen_count = seen + 1

    ctx.send(
        message_builder(target_typename='com.example.fns/inbox',
                        target_id=name,
                        str_value=f"Hello {name} for the {seen}th time!"))

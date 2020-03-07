#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
Life's pathetic, have fun ("▔□▔)/hi~♡ Nasy.

Excited without bugs::

    |             *         *
    |                  .                .
    |           .
    |     *                      ,
    |                   .
    |
    |                               *
    |          |\___/|
    |          )    -(             .              ·
    |         =\ -   /=
    |           )===(       *
    |          /   - \
    |          |-    |
    |         /   -   \     0.|.0
    |  NASY___\__( (__/_____(\=/)__+1s____________
    |  ______|____) )______|______|______|______|_
    |  ___|______( (____|______|______|______|____
    |  ______|____\_|______|______|______|______|_
    |  ___|______|______|______|______|______|____
    |  ______|______|______|______|______|______|_
    |  ___|______|______|______|______|______|____

author   : Nasy https://nasy.moe
date     : Mar  7, 2020
email    : Nasy <nasyxx+python@gmail.com>
filename : bot.py
project  : nasy_nautc_bot
license  : GPL-3.0+

At pick'd leisure
  Which shall be shortly, single I'll resolve you,
Which to you shall seem probable, of every
  These happen'd accidents
                          -- The Tempest
"""

# Telegram
# Other Packages
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import CallbackContext, InlineQueryHandler, Updater
from telegram.update import Update

# Others
from nautc import convert

# Config
from config import TOKEN as BOT_TOKEN


def offset_to_int(offset: str) -> int:
    """Offset string to int."""
    return offset and int(offset) or 0


def convert_it(update: Update, context: CallbackContext) -> None:
    """Convert query text by nautc."""
    print(update.inline_query.query.strip(), update.inline_query.offset, sep="\t")
    update.inline_query.answer(
        list(
            map(
                lambda tc: InlineQueryResultArticle(
                    id=tc[0],
                    title=tc[0],
                    description=tc[1],
                    input_message_content=InputTextMessageContent(tc[1]),
                ),
                convert(update.inline_query.query.strip()),
            )
        )[
            offset_to_int(update.inline_query.offset) : offset_to_int(
                update.inline_query.offset
            )
            + 5
        ],
        cache_time=5,
        next_offset=str(offset_to_int(update.inline_query.offset) + 5),
    )


def main() -> None:
    """Main funcion."""
    bot = Updater(token=BOT_TOKEN, use_context=True)
    bot.dispatcher.add_handler(InlineQueryHandler(convert_it))
    bot.start_polling()


if __name__ == "__main__":
    main()

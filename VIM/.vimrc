# 前回のカーソル位置へ移動する
#
#  痒いところに手が届いた!? vimテク(?)5選  <----- 検索キーワード
#

au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g`\""

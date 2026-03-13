/***************************************************************************
*  這是由輔大化學系製作群所撰寫的遊戲﹐主體由 merc 改編而來﹐所有的版權    *
*  將會被保留﹐但歡迎大家修改﹐但我們也希望你們也能提供給大家﹐所有的商    *
*  業行為將不被允許。                                                      *
*                                                                          *
*  paul@mud.ch.fju.edu.tw                                                  *
*  lc@mud.ch.fju.edu.tw                                                    *
*                                                                          *
***************************************************************************/

#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "merc.h"

extern void       check_contraband args( ( CHAR_DATA * ) );

/* 定義可以到競技場的等級 */
#define LEVEL_CAN_PK               35

/* 定義到競技場要交的錢 */
#define FIGHT_MONEY                10000

/* 定義最小可以去新手區的等級 */
#define LEVEL_NO_NEW               15

DECLARE_JOB_FUN( job_recall_new    );
DECLARE_JOB_FUN( job_goto_pk_area   );
DECLARE_JOB_FUN( job_bore_hole      );
DECLARE_JOB_FUN( job_hit_wall       );
DECLARE_JOB_FUN( job_touch_stone    );
DECLARE_JOB_FUN( job_pray_fire_god  );
DECLARE_JOB_FUN( job_pull_bar       );

#if defined(FUNC_NAME)
#undef FUNC_NAME
#endif

#define FUNC_NAME( nFunction )                             \
  if ( !str_cmp( name, #nFunction ) ) RETURN( nFunction ); \

JOB_FUN * job_lookup( const char * name )
{
  PUSH_FUNCTION( "job_lookup" );
  FUNC_NAME( job_recall_new   );
  FUNC_NAME( job_goto_pk_area );
  FUNC_NAME( job_bore_hole    );
  FUNC_NAME( job_hit_wall     );
  FUNC_NAME( job_touch_stone  );
  FUNC_NAME( job_pray_fire_god );
  FUNC_NAME( job_pull_bar     );
  RETURN( NULL );
}

static bool room_job_target( CHAR_DATA * ch, char * argument
  , const char * keyword, int room_vnum )
{
  char arg[MAX_INPUT_LENGTH];

  if ( !ch || !verify_char( ch ) || !ch->in_room ) return FALSE;
  if ( ch->in_room->vnum != room_vnum ) return FALSE;

  one_argument( argument, arg );

  if ( keyword && *keyword && str_cmp( arg, keyword ) )
  {
    act( "你是要對 $t 做什麼？", ch, ( char * ) keyword, NULL, TO_CHAR );
    return FALSE;
  }

  return TRUE;
}

static bool room_job_move( CHAR_DATA * ch, int room_vnum
  , const char * self_msg, const char * room_msg, const char * arrive_msg )
{
  ROOM_INDEX_DATA * pRoom;

  if ( !ch || !verify_char( ch ) || !ch->in_room
    || !can_char_from_room( ch, TRUE ) ) return FALSE;

  if ( !( pRoom = get_room_index( room_vnum ) ) )
  {
    mudlog( LOG_DEBUG, "room_job_move: 找不到房間 %d。", room_vnum );
    send_to_char( "四周的空間突然扭曲了起來﹐但什麼都沒有發生。\n\r", ch );
    return FALSE;
  }

  if ( room_msg && *room_msg ) act( room_msg, ch, NULL, NULL, TO_ROOM );
  if ( self_msg && *self_msg ) act( self_msg, ch, NULL, NULL, TO_CHAR );

  char_from_room( ch );
  char_to_room( ch, pRoom );

  if ( arrive_msg && *arrive_msg ) act( arrive_msg, ch, NULL, NULL, TO_ROOM );
  do_look( ch, "auto" );
  clear_trace( ch, TRUE );
  return TRUE;
}

JOB( job_recall_new )
{
  ROOM_INDEX_DATA * pRoom;

  PUSH_FUNCTION( "job_recall_new" );

  if ( !( pRoom = RoomSchool )
    || !ch->in_room
    || !can_char_from_room( ch, TRUE ) ) RETURN_NULL();

  if ( ch->level >= LEVEL_NO_NEW )
  {
    send_to_char( "你都已經那麼老了還想去新手區啊﹐真不害臊﹗\n\r", ch );
    RETURN_NULL();
  }

  act( "$n向天神祈禱回到新手區繼續訓練。", ch, NULL, NULL, TO_ROOM );
  send_to_char( "\e[1;33m你狼狽的逃回新手區﹗\e[0m\n\r\n\r", ch );

  char_from_room( ch );
  char_to_room( ch, pRoom );

  act( "$n狼狽的逃了回來﹗", ch, NULL, NULL, TO_ROOM );
  do_look( ch, "auto" );

  /* 清除追蹤紀錄點 */
  clear_trace( ch, TRUE );

  RETURN_NULL();
}

JOB( job_goto_pk_area )
{
  char              buf[MAX_STRING_LENGTH];
  ROOM_INDEX_DATA * pIndex1;
  ROOM_INDEX_DATA * pIndex2;

  PUSH_FUNCTION( "job_goto_pk_area" );

  if ( !ch || !verify_char( ch ) ) RETURN_NULL();

  if ( !( pIndex1 = get_room_index( 7043 ) )
    || !( pIndex2 = get_room_index( 7044 ) ) )
  {
    mudlog( LOG_DEBUG, "job_goto_pk_area: 沒有對戰區." );
    send_to_char( "對不起, 目前系統沒有對戰區.\n\r", ch );
    RETURN_NULL();
  }

  if ( ch->level <= LEVEL_CAN_PK )
  {
    chinese_number( LEVEL_CAN_PK, buf );
    act( "對不起﹐你的等級必須超過$t級才能參加大混戰﹗",
      ch, buf, NULL, TO_CHAR );
    RETURN_NULL();
  }

  if ( get_age( ch ) <= pk_age )
  {
    chinese_number( pk_age, buf );
    act( "對不起﹐你的年齡必須超過$t歲才能參加大混戰﹗",
      ch, buf, NULL, TO_CHAR );
    RETURN_NULL();
  }

  if ( ch->master || ch->leader )
  {
    send_to_char( " 對不起﹐你正跟隨別人﹗\n\r", ch );
    RETURN_NULL();
  }

  if ( auction_info->seller && auction_info->seller == ch )
  {
    send_to_char( "對不起﹐等你賣完東西再來廝殺吧﹗\n\r", ch );
    RETURN_NULL();
  }

  if ( auction_info->buyer && auction_info->buyer == ch )
  {
    send_to_char( "對不起﹐等你買完東西再來廝殺吧﹗\n\r", ch );
    RETURN_NULL();
  }

  if ( ch->jail > 0 )
  {
    send_to_char( "先把你的刑期服完再說吧﹗\n\r", ch );
    RETURN_NULL();
  }

  if ( IS_SET( ch->act, PLR_KILLER )
    || IS_SET( ch->act, PLR_BOLTER )
    || IS_SET( ch->act, PLR_THIEF ) )
  {
    send_to_char( "你如果參加會讓大家知道你跑路的行蹤﹗\n\r", ch );
    RETURN_NULL();
  }

  if ( ch->mount )
  {
    act( "你還在$N上﹐先下馬吧﹗", ch, NULL, ch->mount, TO_CHAR );
    RETURN_NULL();
  }

  if ( ch->spirit )
  {
    act( "對不起﹐你不能帶著$N參加大混戰喔﹗", ch, NULL, ch->spirit, TO_CHAR );
    RETURN_NULL();
  }

  if ( ch->gold < FIGHT_MONEY )
  {
    send_to_char( "你的錢不夠付門票﹗\n\r", ch );
    RETURN_NULL();
  }

  check_contraband( ch );

  act( "天上飄來一朵雲﹐把$n傳送到三國競技場囉﹗", ch, NULL, NULL, TO_ALL );

  sprintf( buf, "%s偷偷的進入了三國競技場, 快去扁他喔!"
    , mob_name( NULL, ch ) );
  talk_channel_2( buf, CHANNEL_PK, "" );

  char_from_room( ch );

  if ( number_percent() > 50 )
    char_to_room( ch, pIndex1 );
  else
    char_to_room( ch, pIndex2 );

  do_look( ch, "auto" );

  /* 清除追蹤紀錄點 */
  clear_trace( ch, TRUE );

  act( "$n來送死囉﹗", ch, NULL, NULL, TO_ROOM );
  gold_from_char( ch, FIGHT_MONEY );

  RETURN_NULL();
}

JOB( job_bore_hole )
{
  PUSH_FUNCTION( "job_bore_hole" );

  if ( !room_job_target( ch, argument, "hole", 1211 ) ) RETURN_NULL();

  room_job_move( ch, 1212
    , "你鼓起勇氣鑽進裂縫之中﹐身體一下子被淡藍色光芒吞沒了。"
    , "$n朝著裂縫一鑽﹐整個人瞬間消失在時空亂流裡。"
    , "$n狼狽地從時空裂縫另一端滾了出來。" );

  RETURN_NULL();
}

JOB( job_hit_wall )
{
  PUSH_FUNCTION( "job_hit_wall" );

  if ( !room_job_target( ch, argument, "wall", 1218 ) ) RETURN_NULL();

  WAIT_STATE( ch, PULSE_VIOLENCE );
  room_job_move( ch, 1219
    , "你奮力朝魔牆猛然一撞﹐耳邊傳來無數冤靈的尖嘯﹐整個人硬是穿了過去。"
    , "$n鼓足勇氣撞向魔牆﹐硬生生衝破了那層陰森的障壁。"
    , "$n從破碎的魔牆另一端跌了進來。" );

  RETURN_NULL();
}

JOB( job_touch_stone )
{
  int shock;

  PUSH_FUNCTION( "job_touch_stone" );

  if ( !room_job_target( ch, argument, "stone", 1224 ) ) RETURN_NULL();

  shock = UMAX( 5, ch->max_hit / 12 );

  act( "$n剛碰到冰玄石﹐就被五星結界震得連退了好幾步。", ch, NULL, NULL, TO_ROOM );
  send_to_char( "你的手指才剛碰到冰玄石﹐五星結界立刻爆出寒流把你震開﹗\n\r", ch );

  if ( can_damage( ch ) )
    damage( ch, ch, shock, TYPE_UNDEFINED, ATTACK_RANDOM );

  WAIT_STATE( ch, PULSE_VIOLENCE );
  RETURN_NULL();
}

JOB( job_pray_fire_god )
{
  int heal;
  int refresh;

  PUSH_FUNCTION( "job_pray_fire_god" );

  if ( !ch || !verify_char( ch ) || !ch->in_room || ch->in_room->vnum != 1233 )
    RETURN_NULL();

  heal    = UMAX( 10, ch->max_hit  / 8 );
  refresh = UMAX( 10, ch->max_move / 6 );

  act( "$n朝著閻羅王神像虔敬膜拜﹐四周翻騰的炎氣像是稍微安靜了下來。"
    , ch, NULL, NULL, TO_ROOM );
  send_to_char( "你誠心向閻羅王祈禱﹐一股力量暫時替你驅散了些許酷熱。\n\r", ch );

  ch->hit  = UMIN( ch->max_hit , ch->hit  + heal );
  ch->move = UMIN( ch->max_move, ch->move + refresh );
  WAIT_STATE( ch, PULSE_VIOLENCE );
  RETURN_NULL();
}

JOB( job_pull_bar )
{
  ROOM_INDEX_DATA * pOuter;
  ROOM_INDEX_DATA * pInner;
  EXIT_DATA       * pOutExit;
  EXIT_DATA       * pInExit;

  PUSH_FUNCTION( "job_pull_bar" );

  if ( !room_job_target( ch, argument, "bar", 1295 ) ) RETURN_NULL();

  if ( !( pOuter = get_room_index( 1289 ) )
    || !( pInner = get_room_index( 1294 ) )
    || !( pOutExit = pOuter->exit[DIR_SOUTH] )
    || !( pInExit = pInner->exit[DIR_NORTH] ) )
  {
    mudlog( LOG_DEBUG, "job_pull_bar: 動物園拉把缺少對應出口。" );
    send_to_char( "你拉動牆上的拉把﹐但遠方只傳來一聲空洞的回響。\n\r", ch );
    RETURN_NULL();
  }

  pOutExit->isdoor = TRUE;
  pInExit->isdoor  = TRUE;
  pOutExit->closed = FALSE;
  pInExit->closed  = FALSE;
  pOutExit->locked = FALSE;
  pInExit->locked  = FALSE;

  act( "$n用力拉下牆上的拉把﹐外頭立刻傳來一聲門閂彈開的脆響。"
    , ch, NULL, NULL, TO_ROOM );
  send_to_char( "你用力一拉﹐只聽見北邊那道門喀啦一聲打開了。\n\r", ch );
  WAIT_STATE( ch, PULSE_VIOLENCE );
  RETURN_NULL();
}
